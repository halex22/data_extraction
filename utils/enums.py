from enum import StrEnum, auto


class TableNames(StrEnum):

    pokedex_data = "Pokédex data"
    base_stats = 'Base stats'
    training = 'Training'
    breeding = 'Breeding'
    pokedex_entries = "Pokédex entries"
    languages = 'Other languages'


class Stats(StrEnum):

    base = auto()
    min = auto()
    max = auto()

# for name in TableNames:
#     print(name.value, name.value)
