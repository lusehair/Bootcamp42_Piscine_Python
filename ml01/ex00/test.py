from book import Book 
from recipe import Recipe

etchebest = Book() 

pateMayo = Recipe("Pate Mayo", 1, 15, "pate et mayo", "lunch", "tres utile en cas de fonsdale") 
TartePruneau = Recipe("Tarte aux pruneaux", 3, 45, "pate sable, pruneaux, confiture, constipation", "dessert") 



etchebest.add_recipe(pateMayo)
etchebest.add_recipe(TartePruneau)
print1 = str(etchebest.get_recipe_by_name("Pate Mayo"))
print2 = str(etchebest.get_recipe_by_types("dessert")) 
print(print1) 
print(print2)