from fastapi import FastAPI

app = FastAPI()
todos = [
    {"id": "1",
     "activity":"Jogging for 2 hours at 7:00 AM."
    },
    {
        "id": "2",
        "activity":"Writing 3 pages of my new book at 2:00 PM."
    }
]

@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"Ping":"Pong"}

@app.get('/todo', tags=['todos'])
async def get_todo() -> dict:
    return {"data": todos}

@app.post("/todo", tags=['todos'])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return {"data": "a todo has been added"}

@app.put("/todo/{id}", tags=['todos'])
async def update_todo(id:int, body:dict) -> dict:
    for todo in todos:
        if int((todo['id'])) == id:
            todo['activity'] = body['activity']
    return {"data": " a todo has been updated"}

@app.delete("/todo/{id}", tags=['todos'])
async def delete_todo(id:int) -> dict:
    for todo in todos:
        if int((todo['id'])) == id:
            todos.remove(todo)
    return {"data": " a todo has been removed"}

