from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI"}

@app.get("/users")
def get_users():
    return {
        "users": ["John", "David", "Alex"]
    }

@app.get('/games')
def get_games():
    return {
        'games':['gta','sony','mee']
    }