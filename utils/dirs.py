import json
from pathlib import Path

POKEMONS_DIR = Path('./pokemon json')


def dir_handler(path_name: Path) -> None:
    """Checks if the dir exits, if not it gets created

    Args: 
        path_name (str): the name to use as dir name.
    """
    if path_name.exists():
        return
    path_name.mkdir()


def save_scrapped_info(destination_dir: Path, file_name: str, info_section: dict) -> None:
    """Saves the information scrapped into a json file

    Args:
        destination_dir (Path): The destination path where the file will be saved
        file_name (str): The name to be given to the file
        info_section (dict): The info to be saved
    """
    target_file = destination_dir / f'{file_name}.json'

    with open(target_file, mode='w', encoding='utf8') as file:
        json.dump(info_section, file, ensure_ascii=False)


if __name__ == '__main__':
    dir_handler(gen_name=POKEMONS_DIR / 'test')
