class Evaluator : 
    
    def zip_evaluate(coefs,words) :
        if coefs == None or words == None or len(coefs) != len(words):
            return -1

        ret : int = 0
        for coef, word in zip(coefs, words) :
            if type(coef) != (int and float) or type(word) != str :
                return -1
            ret = ret + (coef * len(word))
        return (ret) 

    def enumerate_evaluate(coefs, words) :
        if  coefs == None or words == None or len(coefs) != len(words):
            return -1
        ret : int = 0
        for i, word in enumerate(words) :
            if type(coefs[i]) != (int and float) or type(word) != str :
                return -1
            ret = ret + (coefs[i] * len(word))
        return (ret)


if __name__ == '__main__':

    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(coefs, words))


    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.enumerate_evaluate(coefs, words))

    


    words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    print(Evaluator.enumerate_evaluate(coefs, words))

    print(Evaluator.zip_evaluate([0,1],["pas", "le", "chat"]))
    print(Evaluator.enumerate_evaluate([1, 2, 3], ["word", 2, "wordo"])) 

    Evaluator.enumerate_evaluate(None, None)
    Evaluator.zip_evaluate([1, 2, 3], [])
