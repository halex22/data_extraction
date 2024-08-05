from enum import StrEnum


class TableNames(StrEnum):

    pokedex_data = "Pokédex data"
    base_stats = 'Base stats'
    training = 'Training'
    breeding = 'Breeding'
    pokedex_entries = "Pokédex entries"
    languages = 'Other languages'


# for name in TableNames:
#     print(name.value, name.value)
