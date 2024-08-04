from time import sleep

from bs4 import BeautifulSoup, Tag

from path_generator import create_gen_dir, save_pokemon_source_html

BASE_URL = 'https://pokemondb.net'


def find_gen_div(gen_index: int) -> Tag:
    return soup.find('h2', {'id': f'gen-{gen_index}'}).find_next_sibling(
        'div', {'class': 'infocard-list infocard-list-pkmn-lg'}
    )


def get_single_link(div: Tag) -> str:
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
            sleep(2)
            print(f'getting {pokemon_name} info')
            save_pokemon_source_html(
                pokedex_url=f'{BASE_URL}{pokemon_link}', gen_index=gen_index, poke_name=pokemon_name)
