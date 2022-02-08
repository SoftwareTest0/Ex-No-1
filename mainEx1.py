
from tkinter import END
from xmlrpc.client import boolean


def calculate_discount(amount:int,member:boolean):
    if member == False & amount <=2:
        discount=0
    elif member == True & amount <=2:
        discount='20%'    
    elif member == True & amount == 3:
        discount='45%' 
    elif member == False & amount == 3:
        discount='25%' 
    elif member == True & amount >=4 & amount <5:
        discount='53%' 
    elif member == False & amount >=4 & amount <5:
        discount='33%'
    elif member == True & amount >=6 & amount <=10:
        discount='70% '
    elif member == False & amount >=6 & amount <=10:
        discount='50%'
    else:
        print('you can only purchase 10 cartoons')
    return (discount)  

if __name__ == "__main__":
       
    print(calculate_discount(1,True))    
        
        