from typing import List

from bs4 import Tag

from utils.enums import Stats


def get_base_stats_info(table: Tag) -> dict:
    rows: List[Tag] = table.find_all('tr')
    info = {}
    for row in rows:
        stats_info = {}
        results = [_.text for _ in row.find_all(
            'td') if _.text.replace('\n', '')]
        for key, value in zip(Stats, results):
            stats_info[key.name] = int(value)
        info[row.find('th').text.lower()] = stats_info
    return info
