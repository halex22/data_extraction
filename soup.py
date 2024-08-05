from pathlib import Path

from bs4 import BeautifulSoup, Tag

from path_generator import create_gen_dir, save_pokemon_source_html

BASE_URL = 'https://pokemondb.net'
HTML_OUT_BASE = Path('./source')


def find_gen_div(gen_index: int) -> Tag:
    """Simple Function to find the `div` with to get the generation info

    Args:
        gen_index (int): index of the generation desired

    Returns:
        Tag: `div` Tag instance
    """
    return soup.find('h2', {'id': f'gen-{gen_index}'}).find_next_sibling(
        'div', {'class': 'infocard-list infocard-list-pkmn-lg'}
    )


def get_single_link(div: Tag) -> str:
    """Simple function to find the `a` element

    Args:
        div (Tag)

    Returns:
        str: A string with the `href` text
    """
    a_tag = div.find_next('a')
    return a_tag.attrs.get('href')


if __name__ == '__main__':
    gens_list = [_ for _ in range(1, 10)]

    with open('./html_source.html', 'r', encoding='utf8') as file:
        source = file.read()

    soup = BeautifulSoup(source, 'html.parser')

    for gen_index in gens_list:

        list_div = find_gen_div(gen_index=gen_index)
        create_gen_dir(gen_index=gen_index)
        for div in list_div.find_all('div', {'class': 'infocard'}):
            pokemon_link = get_single_link(div=div)
            pokemon_name = pokemon_link.split('/')[-1]
            pokemon_html_file_path = HTML_OUT_BASE / \
                f'gen_{gen_index}' / f'{pokemon_name}.html'
            if pokemon_html_file_path.exists():
                print(f'{pokemon_name} file already exits')
                continue
            print(f'getting {pokemon_name} info')
            save_pokemon_source_html(
                pokedex_url=f'{BASE_URL}{pokemon_link}', file_path=pokemon_html_file_path)
