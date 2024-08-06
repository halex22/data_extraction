from dataclasses import dataclass, field
from typing import Dict, List, Union

from bs4 import BeautifulSoup, PageElement, ResultSet, Tag

from additional_info import (extract_tr_many, get_evolutions, get_src_attr,
                             get_types_effect)
from additional_info.base_stats import get_base_stats_info
from utils.enums import TableNames


def clean_tn_data(table_name: str) -> str:
    """Strips the name from unwanted characters"""
    result = table_name.replace(' №', '').replace(
        ' ', '_').replace('.', '').lower()
    return result


def get_current_pokemon_name(soup_instance: BeautifulSoup) -> str:
    return soup_instance.find('h1').text.split(' (')[0]


def get_general_data(soup_instance: BeautifulSoup, tables: Union[List[str], str]) -> dict:
    """Extract the info from the tables in the `TableNames` enum subclass from the utils
    module.

    Args:
        soup_instance (BeautifulSoup): The html source code parsed into a bs4 instance

    Returns:
        dict: dict containing the info ready to be parsed into json format 
    """
    data = {}
    where_to_find_table_name = f'Where to find {get_current_pokemon_name(soup_instance)}'
    sections_name = soup_instance.find_all('h2')

    tables_to_search = [
        _.value for _ in TableNames] if tables == 'all' else tables

    for table_name in tables_to_search:
        table_info = get_table_info(
            sections=sections_name, table_name=table_name)
        data[clean_tn_data(table_name)] = table_info

    data['where_to_find'] = get_table_info(
        sections=sections_name, table_name=where_to_find_table_name, where_to_find=True)

    return data


def get_additional_info(soup: BeautifulSoup) -> dict:
    data = {}
    data['evolutions'] = get_evolutions(soup=soup)
    data['img_link'] = get_src_attr(soup=soup)
    data['types_effect'] = get_types_effect(soup=soup)
    return data


def get_table_info(table_name: str, sections: ResultSet, where_to_find: bool = False) -> dict[str, str]:

    table_info = {}
    pokedex_data_table = get_desired_table(sections, filter=table_name)

    if not pokedex_data_table:
        return {table_name: None}

    if table_name == TableNames.pokedex_entries or where_to_find:
        return extract_tr_many(table=pokedex_data_table)

    if table_name == TableNames.base_stats:
        return get_base_stats_info(table=pokedex_data_table)

    rows = pokedex_data_table.find_all('tr')
    for row in rows:
        name, value = extract_table_row_info(row)
        name = clean_tn_data(name)
        table_info[name] = value

    return table_info


def get_desired_table(result: list[PageElement], filter: str) -> Union[Tag, None]:
    """Filters all the tables found and return the one matching the filter given

    Args:
        result (list[PageElement]): Array of `h2` elemetns
        filter (str): Name of the table to extract from the array.

    Returns:
        Union[Tag, None]: the next `tbody` element in the soup if available
    """
    for _ in result:
        if _.text == filter:
            return _.find_next('tbody')
    return None


def extract_table_row_info(row: PageElement) -> None:
    """Takes a row and extract the text from the `th`  and the `td` elements """
    row_name = row.find_next('th').text
    row_value = row.find_next('td').text.replace('\n', ' ').replace('\xa0', '')
    return row_name, row_value


@dataclass
class InfoExtractor:
    soup: BeautifulSoup
    extracted_info: Dict[str, str] = field(init=False, default_factory={})

    def __post_init__(self):
        ...
