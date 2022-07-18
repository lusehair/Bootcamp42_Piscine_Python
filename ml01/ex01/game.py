
class GotCharacter:
    first_name = "" 
    is_alive = True

    def __init__(self, first_name, is_alive = True) :
        self.first_name = first_name
        self.is_alive = is_alive
        


class Lannister(GotCharacter) :
    """Generic class for GoT Character from Lannister Family"""
    family_name =""
    house_words = ""

    def __init__(self, first_name=None, is_alive=True) : 
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "Coors from root"
    
    def print_house_words(self) :
        print(self.house_words) 
    
    def die(self) :
        self.is_alive = False
    
