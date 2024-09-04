from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange


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


@app.get("/")
def get_user():
    return {"Hello": "welcome fastapi"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 300)
    print(post_dict)
    my_posts.append(post_dict)
    return {"data": my_posts}


@app.get("/posts/{id}")
def get_single_post(id):
    single_post = {}

    for p in my_posts:
        if p["id"] == int(id):
            single_post = p
            print(single_post)

    return {"post_details": single_post}
