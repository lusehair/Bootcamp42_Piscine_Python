import os 





def ft_progress(lst) :
    ETA = 12.12
    ELT = 15.20
    bar = ''
    
    percent = (ret / len(lst)) * 100
    print("ETA: " + "{:.2e}".ETA + 's [' + str(percent) + '%][', end='') # ETA: 8.65s [23%][
    print("]", end='') # ====>]
    print(str(ret) + '/' + str(len(lst)) + ' | elapsed time ' + str(ELT) + 's') # 233/3333 | elapsed time 2.33s 
    


listy = range(3333)
ret = 0 