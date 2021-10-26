#A shop will give discount of 50% if the cost of purchased quantity is more than 10000.
#  Ask user for quantity suppose, one unit will cost 100. Judge and print total cost for user.

x = int(input("Enter quantity to be purchased:"))
cost = x*100

if cost > 10000:
    cost/=2
    print("Cost = ",cost ) 
else:
    print("Cost = ", cost)