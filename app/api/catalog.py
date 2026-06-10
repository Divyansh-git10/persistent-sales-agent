import json

from fastapi import APIRouter

router = APIRouter()


@router.get("/catalog")
def get_catalog():

    with open("app/data/catalog.json", "r") as f:

        catalog = json.load(f)

    return catalog