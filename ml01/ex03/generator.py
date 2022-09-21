import random 

def generator(text, sep=" ", option=None):
    

    options : list = ['shuffle', 'ordered', 'unique']
    quotelist : list = []

    # def __init__(self) :

        # Handle errors 
    if text == '' or type(text) != str : 
        quotelist.append('ERROR')
    
    elif option != None: 
        if type(option) != str or options.count(option) == 0 :
            quotelist.append('ERROR')
    if len(quotelist) == 1 :
        yield(quotelist)
    

    else :
        quotelist = text.split(sep) 
        i = -1
        if option == None : 
            while(i < len(quotelist)) : 
                yield quotelist[i]
                i = i + 1
        elif option == 'shuffle': 
            shuffleQuote = []
            while len(quotelist) :
                word = random.choice(quotelist) 
                #print("the len :", len(shuffleQuote))
                shuffleQuote.append(word)
                quotelist.remove(word)
                #print(shuffleQuote) 
            while i < len(shuffleQuote) :
                yield shuffleQuote[i] 
                i = i + 1
    
        elif option == 'unique' : 
            i = 0
            ret = []
            while  i < len(quotelist):
                if quotelist[i] not in ret :
                    ret.append(quotelist[i])
                i = i + 1
            i = 0
            
            while i < len(ret) :
                yield ret[i] 
                i = i + 1

        
        elif option == 'ordered' : 
            print("here")
            quotelist.sort()
            i = 0 
            while i < len(quotelist) :
                yield quotelist[i] 
                i = i + 1
            


if __name__ == '__main__':


    text = 0.1
    #text = "This is a simple string for a basic test. Very simple."
    for word in generator(text, sep=' ', option='ordered') :
        print(word) 
        


