



# 100 stock 
# 1stock =10rs

stock=100
while True:

    user=int(input('''
        1] display the available stocks
        2] Request bike for rent (1 Qty =10rs)
        3] Exit

'''))

    if(user==1):
        print("available stock are :",stock)
    
    elif(user==2):
        uprice=int(input())

        Qty=uprice//10

        stock=stock-Qty

        print("Amount you paid for bike rent is:",uprice)
        print("Qty of Bike open's are:  ",Qty)

    else:
        print("will buy, next time thankyou ")
        break



