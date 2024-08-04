from pathlib import Path

POKEMONS_DIR = Path('./pokemon json')


def gen_dir_handler(path_name: Path) -> None:
    """Checks if the dir exits, if not it gets created

    Args: 
        gen_name (str): the name of the generation to use as dir name.
    """
    if path_name.exists():
        return
    path_name.mkdir()


if __name__ == '__main__':
    gen_dir_handler(gen_name=POKEMONS_DIR / 'test')
