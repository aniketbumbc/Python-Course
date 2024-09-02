from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def get_user():
    return {"Hello": "welcome fastapi"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}


@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"title": payload['title'], "content": payload['content']}
