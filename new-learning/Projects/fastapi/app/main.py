from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from starlette.responses import Response
import time


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


while True:
    try:
        conn = psycopg2.connect(
            host='localhost', database='fastapi', user='postgres', password='123', port=5432, cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection successful")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error: ", error)
        time.sleep(4)


my_posts = [{"title": " title post 1", "content": "contnet of post", "id": 1},
            {"title": "what to eat for dinner ?",
             "content": "Vggies with less fat and carbs",
             "id": 2}]


def find_post(id):
    for p in my_posts:
        if p["id"] == int(id):
            return p


def find_index_post(id):
    for obj in my_posts:
        if (obj['id'] == id):
            ele_index = my_posts.index(obj)
            return ele_index


@app.get("/")
def get_user():
    return {"Hello": "welcome fastapi"}

# Get all posts


@app.get("/posts")
def get_posts():
    cursor.execute("""  SELECT * FROM posts    """)
    posts = cursor.fetchall()
    return {"data": posts}


# Create post

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute(
        """  INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
        (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()

    return {"data": new_post}


# Get single post


@app.get("/posts/{id}")
def get_single_post(id: int, resp: Response):
    cursor.execute("""  SELECT * FROM posts WHERE ID = %s """, (str(id)))
    single_post = cursor.fetchone()
    if not single_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id {id} was not found')
    return {"post_details": single_post}


# Delete single post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute(
        """  DELETE FROM posts WHERE ID = %s returning *""", (str(id)))
    delete_post = cursor.fetchone()
    conn.commit()
    if (delete_post == None):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f'wrong post with id {id}')

    return Response(status_code=status.HTTP_204_NO_CONTENT)

# update single post


@app.put("/posts/{id}")
def updatePost(id: int, post: Post):
    cursor.execute(
        """  update posts set title = %s, content = %s , published = %s where id = %s RETURNING * """,
        (post.title, post.content, post.published, str(id)))

    updated_post = cursor.fetchone()
    conn.commit()
    if (updated_post == None):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f'wrong post with id {id}')

    return {"data": updated_post}
