
from conn_db import *
from models import People

people = Table('people')
########### GET ##############################
def controller_get_people():
    sql = Query.from_(people).select('*')
    r = select_db(sql)
    return r

def controller_get_people_id(id: int):
    sql = Query.from_(people).select('name').where(people.id==id)
    r = select_db(sql)
    return r

########### POST ##############################
def controller_create_people(person: People):
    sql = Query.into(people) \
    .columns('name', 'email','whatsapp','city', 'uf') \
    .insert(person.name, person.email,person.whatsapp,person.city,person.uf) 
    print(str(sql))
    query_db(sql)

########### PUT ##############################
def controller_update_people(id: int, person:People):
    
    sql = Query.from_(people).select('id').where(people.id==id)
    resp = select_db(sql)

    if(resp==[]):
        return {'error':"id não existe"}
    
    sql = Query.update(people).set(people.name, person.name ).where(people.id == id)
    
    if(person.email):
        sql.set(people.email, person.email )

    if(person.whatsapp):
        sql.set(people.whatsapp, person.whatsapp )

    if(person.city):
        sql.set(people.city, person.city )

    if(person.uf):
        sql.set(people.uf, person.uf )


    print(sql)
    # sql = f'''
    # UPDATE people
    # SET name = '{person.name}',
    #     email = '{person.email}',
    #     whatsapp = '{person.whatsapp}',
    #     city = '{person.city}',
    #     uf = '{person.uf}'
    # WHERE id = {id};
    #     '''
    query_db(sql)

    sql = Query.from_(people).select('*').where(people.id == id)
    r = select_db(sql)

    return(r[0])


########### DELETE ##############################
def controller_delete_people(id: int):
    
    sql = Query.from_(people).select('id').where(people.id==id)
    id = select_db(sql)

    if(id==[]):
        return {'error':"id não existe"}

    id = id[0][0]
    
    sql = Query.from_(people).delete().where(people.id == id)
    query_db(sql)

    return{'status':204}
