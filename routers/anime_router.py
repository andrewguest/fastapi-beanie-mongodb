from typing import List, Optional

from fastapi import APIRouter, HTTPException

from models.anime_models import AnimeEntry

router = APIRouter(tags=["anime"])


@router.post("/anime", response_model=AnimeEntry)
async def create_anime(anime: AnimeEntry):
    await anime.insert()
    return anime


@router.get("/", response_model=List[AnimeEntry])
@router.get("/anime", response_model=List[AnimeEntry])
async def read_anime(limit: Optional[int] = 20):
    anime = await AnimeEntry.find_all().limit(limit).to_list()

    return anime


@router.get("/anime/{anime_id}", response_model=AnimeEntry)
async def read_task(anime_id: str):
    anime = await AnimeEntry.find_one({"_id": anime_id})
    print(anime)
    if not anime:
        raise HTTPException(status_code=404, detail="AnimeEntry")
