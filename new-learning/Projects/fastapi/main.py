from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

from starlette.responses import Response


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": " title post 1", "content": "contnet of post", "id": 1},
            {"title": "what to eat for dinner ?",
             "content": "Vggies with less fat and carbs",
             "id": 2}]


def find_post(id):
    for p in my_posts:
        if p["id"] == int(id):
            return p


@app.get("/")
def get_user():
    return {"Hello": "welcome fastapi"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 300)
    print(post_dict)
    my_posts.append(post_dict)
    return {"data": my_posts}


@app.get("/posts/{id}")
def get_single_post(id: int, resp: Response):
    single_post = find_post(id)
    if not single_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id {id} was not found')
    return {"post_details": single_post}
