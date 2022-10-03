
import math 

class TinyStatistician() :
    

    def mean(self, x) :
        if x is None: return None
        return sum(x) / len(x) 

    def median(self, x) :
        if x is None: return None 

        x.sort() 
        if len(x) % 2 == 0:
            med1 = x[len(x)//2]
            med2 = x[len(x)//2 - 1]
            return (med1 + med2)/2 
        else :
            return x[len(x)//2]
    

    def quartile(self, x) :
        if x is None :  return None 
        x.sort()
       
       # Quartile One 
        pos = len(x) // 4
        if len(x) % 4 < 2:
            q1 = (x[pos-1] + x[pos])/2 
        else :
            q1 = x[pos-1]

        # Quartile Three 
        pos = 3 * len(x) // 4 
        if len(x) % 4 < 2:
            q3 = (x[pos] + x[pos + 1]) / 2
        else : 
            q3 = x[pos]
        
        return q1, q3


    def var(self, x) : 
        if x is None: return None 
        
        mean = sum(x)/len(x)  
        total = 0.0
        for value in x: 
            total = total + (value - mean)**2 
        return total/len(x) 
    
    def std(self, x) : 
        if x is None: return None 
        
        mean = sum(x) / len(x)
        var  = sum(pow(value-mean,2) for value in x) / len(x) 
        return  math.sqrt(var)   


if __name__ == "__main__":

    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    print(tstat.mean(a))
    # Expected result: 82.4
    print(tstat.median(a))
    # Expected result: 42.0
    print(tstat.quartile(a))
    # Expected result: [10.0, 59.0]
    print(tstat.var(a))
    # Expected result: 12279.439999999999
    print(tstat.std(a))
    # Expected result: 110.81263465868862 




