class Recipe: 
    name = ""
    cooking_lvl= 1
    cooking_time = 1
    ingredients = []
    description = ""
    recipe_type = ""
    _type_list = ["starter", "lunch", "dessert"]

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name 
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type 
        try :
            self.cooking_lvl = int(cooking_lvl)
            self.cooking_time = int(cooking_time)
        
        except:
            print("The time and/or the cooking level is not a integer")

        if self.cooking_lvl < 1 or self.cooking_lvl > 5 :
            print("The cooking level is out of range")
            return 
        elif self.cooking_time < 0 : 
            print("The cooking time cannot be negative")
            return 
        elif self._type_list.count(recipe_type) == 0 :
            print("the recipe time doesn't exist")
            return 
    
    def __str__(self) :
        txt = "Recipe for " + self.name + ". His cooking level is " + int(self.cooking_lvl)
        txt = txt + " , you need" + int(self.cooking_time) + " minutes for cook this. Of course you need : "
        txt = txt + self.ingredients + " . It can be eat " + self.recipe_type 
        return txt 

     