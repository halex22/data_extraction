from bs4 import BeautifulSoup, PageElement, ResultSet, Tag

from additional_info import (get_evolutions, get_languages, get_src_attr,
                             get_types_effect)
from utils.enums import TableNames


def clean_tn_data(table_name: str) -> str:
    """Strips the name from unwanted characters"""
    result = table_name.replace(' №', '').replace(' ', '_').replace('.', '').lower() 
    return result


def get_general_data(soup_instance: BeautifulSoup) -> dict:
    data = {}
    sections_name = soup_instance.find_all('h2')
    for table_name in TableNames:
        table_info = get_table_info(
            sections=sections_name, table_name=table_name)
        data[table_name.name] = table_info
    data['evolutions'] = get_evolutions(soup=soup_instance)
    data['languages'] = get_languages(soup=soup_instance)
    data['img_link'] = get_src_attr(soup=soup_instance)
    data['types_effect'] = get_types_effect(soup=soup_instance)
    return data


def get_table_info(table_name: str, sections: ResultSet) -> dict[str, str]:
    table_info = {}
    try:
        pokedex_data_table = get_desired_table(sections, filter=table_name)
        rows = pokedex_data_table.find_all('tr')
        for row in rows:
            name, value = extract_table_row_info(row)
            name = clean_tn_data(name) if table_name != TableNames.pokedex_entries else name
            table_info[name] = value
    except ValueError:
        table_info[table_name] = None
    return table_info


def get_desired_table(result: list[PageElement], filter: str) -> Tag:
    """Filters all the tables found and return the one matching the filter given"""
    for _ in result:
        if _.text == filter:
            return _.find_next('tbody')
    raise ValueError(f'No section named -- {filter} -- was found')


def extract_table_row_info(row: PageElement) -> None:
    """Takes a row and extract the text from the `th`  and the `td` elements """
    row_name = row.find_next('th').text
    row_value = row.find_next('td').text.replace('\n', ' ').replace('\xa0', '')
    return row_name, row_value
