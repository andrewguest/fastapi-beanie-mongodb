from beanie import Document
from pydantic import BaseModel


class AnimeEntry(Document, BaseModel):
    class Settings:
        name = "anime"

    # Beanie will automatically handle the `id` field (_id)

    title: str
    type: str
    episodes: int
    status: str
    animeSeason: dict
    picture: str
    thumbnail: str
    synonyms: list
    relations: list
    tags: list
    sources: list
