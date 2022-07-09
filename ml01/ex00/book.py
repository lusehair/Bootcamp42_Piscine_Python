import datetime


class Book:
    name =""
    last_update =  datetime.datetime.now()
    creation_date = datetime.datetime.now()
    recipes_list= { 
        'starter' : {}, 
        'cake' : {}, 
        'salad' : {}
    } 

