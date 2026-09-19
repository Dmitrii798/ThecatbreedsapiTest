# data/sources/breed_dataclass.py
from dataclasses import dataclass


@dataclass
class Breed:
    id: str
    name: str
    origin: str | None = None
    temperament: str | None = None
    life_span: str | None = None
    wikipedia_url: str | None = None
   