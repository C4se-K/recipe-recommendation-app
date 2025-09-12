from pydantic import BaseModel

class Feedback(BaseModel):
    user_id: str
    recipe_id: str
    liked: bool 