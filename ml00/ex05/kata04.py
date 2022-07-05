from decimal import Decimal 

t = ( 0, 4, 132.42222, 10000, 12345.67) 

print('module_' + str(t[0]).zfill(2) + ', ex_' + str(t[1]).zfill(2) + ' : ' + '%.2f'%t[2] + ', ' + "{:.2e}".format(t[3]) + ', '+ "{:.2e}".format(t[4]))