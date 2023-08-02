from pydantic import BaseModel


class Post(BaseModel):
	post_id: int
	post_rating: int
	title: str


class Root(BaseModel):
	name: str
	post: list[Post]
	rating: int
	registration_at: str


