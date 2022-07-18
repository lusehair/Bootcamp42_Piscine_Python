import datetime
from recipe import Recipe

class Book:
    name =""
    last_update =  datetime.datetime.now()
    creation_date = datetime.datetime.now()
    recipes_list= {
        'starter' : [], 
        'lunch' : [],
        'dessert' : []
    } 

    def get_recipe_by_name(self, name) :
        for _, recipes in self.recipes_list.items() :
            for recipe in recipes :
                if recipe._name == name : 
                    return recipe
    

    def get_recipe_by_types(self, type) :
        ret = []
        for meal, recipes in self.recipes_list.items() : 
            if meal == type:
               for recipe in recipes :
                ret.append(recipe._name)
        return ret 

        
    def add_recipe(self, recipe) :
        if isinstance(recipe, Recipe) == False :
            print("Error: the type of object is not a Recipe")
            return 
        if recipe._recipe_type == 'starter' :
            self.recipes_list["starter"].append(recipe)
        elif recipe._recipe_type == 'lunch' :
            self.recipes_list["lunch"].append(recipe) 
        elif recipe._recipe_type == 'dessert' :
            self.recipes_list["dessert"].append(recipe) 
        self.last_update = datetime.datetime.now()
        