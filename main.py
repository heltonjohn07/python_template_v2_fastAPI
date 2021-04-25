
from fastapi import FastAPI
from conn_db import *
from pypika import *
from models import People
from Controllers import *

app = FastAPI()
authors = Table('people')

#models
print('\n\n Server Running......\n\n')

#Rota Raiz
@app.get('/')
def index():
    return {"Welcome": "To API"}

@app.post('/v2/people', response_model = People)
def create_people(author: People):
    return controller_create_people(author)
    
@app.get('/v2/people')
def get_all_people():
    return controller_get_people()

@app.get('/v2/people/{id}')
def get_people_by_id(id: int):
    return controller_get_people_id(id)

@app.put('/v2/people/{id}')
def update_people_by_id(id: int, person:People):
    return controller_update_people(id, person)

@app.delete('/v2/people/{id}')
def delete_people_by_id(id: int):
    return controller_delete_people(id)
    
    


