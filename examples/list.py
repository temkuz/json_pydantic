from pydantic import BaseModel


class ContentList(BaseModel):
    id: int
    text: str
    

class Root(BaseModel):
    content_list: list[ContentList]
    
