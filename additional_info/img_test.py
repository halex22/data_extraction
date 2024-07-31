from pathlib import Path

from bs4 import BeautifulSoup, Tag

path_dir = Path('./source/gen_1')


def get_src_attr(soup: BeautifulSoup) -> str:
    try:
        anchor_tag_target: Tag = soup.find('a', attrs={'rel':'lightbox'})
        pokemon_img: Tag = anchor_tag_target.find('img')
        return pokemon_img.get(key='src', default=None)
    except AttributeError:
        return None


for _ in path_dir.iterdir():

    with open(_, mode='r', encoding='utf8') as file:
        source_code = file.read()

    soup = BeautifulSoup(source_code, 'html.parser')

    print(get_src_attr(soup=soup))