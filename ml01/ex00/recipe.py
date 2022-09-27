class Recipe: 
    _name = ""
    _cooking_lvl= 1
    _cooking_time = 1
    _ingredients = []
    _description = ""
    _recipe_type = ""
    _type_list = ["starter", "lunch", "dessert"]

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description=None, recipe_type=None):
        self._name = name 
        self._ingredients = ingredients
        self._description = description
        self._recipe_type = recipe_type 
        try :
            self._cooking_lvl = cooking_lvl
            self._cooking_time = int(cooking_time)
        
        except:
            print("The time and/or the cooking level is not a integer")

        if type(self._cooking_lvl) != int :
            print("the cooking level should be a int")
            return 

        if self._cooking_lvl < 1 or self._cooking_lvl > 5 :
            print("The cooking level is out of range") 
            return 
        elif self._cooking_time < 0 : 
            print("The cooking time cannot be negative")
            return 
        print(self._recipe_type)
        if self._type_list.count(self._recipe_type) == 0 :
            print("the recipe time doesn't exist")
            return 
        
        if len(self._ingredients) == 0 :
            print("you cannot have empty ingredients list")
            return 
    
    def __str__(self) :
        txt = "Recipe for " + self._name + ". His cooking level is " + str(self._cooking_lvl)
        txt = txt + " , you need " + str(self._cooking_time) + " minutes for cook this. Of course you need : "
        txt = txt + str(self._ingredients) + " . It can be eat " + self._recipe_type 
        return txt 

    

     