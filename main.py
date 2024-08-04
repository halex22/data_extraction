from pathlib import Path

from bs4 import BeautifulSoup

from utils.dirs import gen_dir_handler

OUTPUT_DIR = Path('./pokemon json')
INPUT_DIR = Path('./source')

if __name__ == '__main__':

    for generation in INPUT_DIR.iterdir():
        gen_index = generation.name[-1]

        print(f'Extracting generation {gen_index} info')
        gen_target = OUTPUT_DIR / f'gen_{gen_index}'
        gen_dir_handler(path_name=gen_target)

        for pokemon_file in generation.iterdir():
            # with open(pokemon_file, mode='r', encoding='utf8') as file:
            #     source_code = file.read()

            # soup = BeautifulSoup(source_code, 'html.parser')
            print(pokemon_file)
