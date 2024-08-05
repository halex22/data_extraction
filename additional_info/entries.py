from typing import List

from bs4 import Tag


def extract_tr_many(table: Tag) -> dict:
    """Extract the info when there are many `span` tags in the `th` tag

    Args:
        table (Tag): `tbody` tag 

    Returns:
        dict: dict containing one key for every `span` tag 
    """
    info = {}
    rows: List[Tag] = table.find_all('tr')
    for row in rows:
        for game in row.find_all('span'):
            info[game.text] = row.find('td').text
    return info
