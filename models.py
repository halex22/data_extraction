from typing import List, Union

from pydantic import BaseModel


class StatsModel(BaseModel):
    hp: int
    attack: int
    deffense: int
    sp_atk: int
    sp_def: int
    speed: int
    total: int


class BasePokemonModel(BaseModel):
    id: int
    name: str
    types: Union[str, tuple[str, str]]


class PokemonModel(BasePokemonModel):
    height: float
    weight: float
    abilities: List[str]
    stats: StatsModel
