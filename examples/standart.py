from pydantic import BaseModel


class FilledStruct(BaseModel):
    code: int
    message: str
    

class Post(BaseModel):
    post_id: int
    title: str
    post_rating: int
    

class Root(BaseModel):
    name: str
    registration_at: str
    rating: int
    post: list[Post]
    filled_struct: FilledStruct
    empty_struct: dict
    
