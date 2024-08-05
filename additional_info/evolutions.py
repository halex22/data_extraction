from itertools import zip_longest
from pathlib import Path
from typing import Dict, List, Union

from bs4 import BeautifulSoup, Tag

path_dir = Path('./source/gen_1')

test_set = True


def one_ev_line(div: Tag):
    """Function to fetch info from one evolution line pokemon"""
    info_list: List[Tag] = div.find_all('div', attrs={'class': 'infocard'})
    levels_list: List[Tag] = div.find_all(
        'span', attrs={'class': 'infocard-arrow'})
    poke_ev_dict = {}

    for combo in zip_longest(info_list, levels_list):
        poke_ev_dict[combo[0].text.split(
            ' ')[1]] = combo[1].text if combo[1] else ''

    return poke_ev_dict


def get_evolutions(soup: BeautifulSoup) -> dict:
    """Function to get the pokemon evolution"""
    ev_divs: List[Tag] = soup.find_all(
        'div', attrs={'class': 'infocard-list-evo'})
    if ev_divs:
        if len(ev_divs) == 1:
            return one_ev_line(ev_divs[0])
        ev_lines = []
        for div in ev_divs:
            ev_lines.append(one_ev_line(div))
        return ev_lines
    return None


if __name__ == '__main__':

    if test_set:

        for _ in path_dir.iterdir():

            with open(_, mode='r', encoding='utf8') as file:
                source_code = file.read()

            soup = BeautifulSoup(source_code, 'html.parser')

            print(get_evolutions(soup=soup))

    else:
        test_file = next(path_dir.iterdir())
        with open(test_file, mode='r', encoding='utf8') as file:
            source_code = file.read()

        soup = BeautifulSoup(source_code, 'html.parser')
        print(get_evolutions(soup=soup))
