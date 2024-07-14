from enum import StrEnum, auto


class TableNames(StrEnum):

    pokedex_data =  "Pokédex data"
    base_stats = 'Base stats'
    trainig = 'Training'
    breeding = 'Breeding'

# for name in TableNames:
#     print(name.value, name.value)