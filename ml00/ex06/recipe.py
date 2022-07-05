import os 

cookBook = {
    'sandwich' : {'title' : 'sandwich', 'ingredients' : ' ham, bread, cheese and tomatoes', 'meal' : 'lunch', 'prep_time' : '10'},
    'cake' : {'title' : 'cake', 'ingredients' : ' flour, sugar and eggs', 'meal' : 'dessert', 'prep_time' : '60'}, 
    'salad' : {'title' : 'salad', 'ingredients' : 'avocado, arugula, tomatoes and spinach.', 'meal' : 'lunch', 'prep_time' : '15'}
}


def listRecipe() :
    for key in cookBook :
        print(key)


def delRecipe() :
    lostRecipe = ''
    os.system('clear')
    listRecipe()
    lostRecipe = input("Please, write the recipe to delete: ")
    if lostRecipe in cookBook :
        del cookBook[lostRecipe]
    else : 
        delRecipe()



def addREcipe():

    _title = ''
    _ingredients = ''
    _meal = ''
    _prep_time = ''

    # os.system('clear')
    _title = input("The name of your meal: ")
    _ingredients = input("List of ingredients: ")
    _meal = input("Type of meal: ")
    _prep_time = input("The prep time (in minutes): ")

    cookBook[_title] = dict(title = _title, ingredients = _ingredients, meal = _meal, prep_time = _prep_time)



def printRecipe(): 

    theRecipe = ''
    # os.system('clear')
    theRecipe = input('What i want to cook ') 
    if theRecipe in cookBook:
        print("Recipe for " + cookBook[theRecipe]['title'] + ':') 
        print("Ingredients list: " + cookBook[theRecipe]['ingredients'])
        print('To be eaten for ' + cookBook[theRecipe]['meal'])
        print("Takes " + cookBook[theRecipe]['prep_time'] + " minutes of cooking.")
    else :
        printRecipe()

def menu():
    while True:
        choice = ''
        # os.system('clear')
        print("Please select an option by typing the corresponding number:") 
        print("1: Add a recipe \n 2: Delete a recipe \n 3: Print a recipe \n 4: Print the cookbook \n 5: Quit\n >>", end='')
        choice = input()

        if choice == '1':
            addREcipe()
        elif choice == '2':
            delRecipe()
        elif choice == '3':
            printRecipe()
        elif choice == '4':
            # os.system('clear')
            listRecipe()
        elif choice == '5':
            return 0
        else :
            menu()

menu()