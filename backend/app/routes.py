from fastapi import APIRouter, Query
import requests
from .models import Feedback
#from

router = APIRouter(prefix="/api.recipies")

@router.get("/")
def get_recipies():

    return


@router.post("/feedback")
def post_feedback():
    return