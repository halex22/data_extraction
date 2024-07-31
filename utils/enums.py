from enum import StrEnum, auto


class TableNames(StrEnum):

    pokedex_data =  "Pokédex data"
    base_stats = 'Base stats'
    training = 'Training'
    breeding = 'Breeding'
    pokedex_entries = "Pokédex entries"


# for name in TableNames:
#     print(name.value, name.value)