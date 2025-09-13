from fastapi import APIRouter, Query
import requests
from .models import Feedback
#from
import jsonify

router = APIRouter(prefix="/api.recipies")

@router.get("/")
def status():
    return {'status':'OK'}

@router.get("/recipe")
def get_recipies(query: str = Query(None), exclude: str = Query(None)):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query or ''}"
    if not query:
        url = f"https://www.themealdb.com/api/json/v1/1/random.php"

    response = requests.get(url)
    recipes = response.json().get('meals', [])

    if exclude:
        recipes = [meal for meal in recipes if not any(exclude.lower() in val.lower() for val in meal.values()if val)]

    return recipes


@router.post("/feedback")
def post_feedback():
    return