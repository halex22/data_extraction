import requests


def get_source_html_code(url: str = 'https://pokemondb.net/pokedex/national') -> None:
    """Gets the pokedex source file. 

    Args:
        url (str, optional): The url to make the request. Defaults to 'https://pokemondb.net/pokedex/national'.
    """
    res = requests.get(url=url)
    target_file = './html_source.html'
    with open(target_file, 'w', encoding='utf8') as file:
        file.write(res.text)


if __name__ == '__main__':
    get_source_html_code()
