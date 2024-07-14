from bs4 import BeautifulSoup, PageElement, ResultSet, Tag

from utils.enums import TableNames


def get_general_data(soup_instance: BeautifulSoup) -> dict:
    data = {}
    sections_name = soup_instance.find_all('h2')
    pokedex_data_table = get_desired_table(sections_name, "Pokédex data")
    rows = pokedex_data_table.find_all('tr')
    for row in rows:
        name, value = extract_table_row_info(row)
        data[name] = value
    print(data)


# def get_table_info(table_name: str, sections: ResultSet):
#     pokedex_data_table = get_desired_table(sections, filter=table_name)
#     rows = pokedex_data_table.find_all('tr')
#     for row in rows:
#         name, value = extract_table_row_info(row)
#         data[name] = value


def get_desired_table(result: list[PageElement], filter: str ) -> Tag :
    for _ in result:
        if _.text == filter: 
            return _.find_next('tbody')
    raise ValueError(f'No section named -- {filter} -- was found')


def extract_table_row_info(row: PageElement) -> None:
    row_name = row.find_next('th').text
    row_value = row.find_next('td').text.replace('\n', ' ').replace('\xa0', '')
    return row_name, row_value


    

