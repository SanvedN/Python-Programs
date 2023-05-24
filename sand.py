print("Welcome to MySandwitch !!")
n=int(input("Enter the number of sandwitches that you want to order : "))
print('''Toppings available are :
1. Onions
2. Lettuce
3. Tomato
4. Olives
5. Peppers''')
t = [input('Enter any three of the toppings by their number : ').split()]
print("You have ordered ",n,"sandwitches. Total bill is : ",(n*5),"$")