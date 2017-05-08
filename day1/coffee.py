""" Make coffe 
1. Took a cup
2. poured coffee into the cup
3. added sugar
4. pour milk
5. Stir
6. ready to serve
"""

# Make coffee cup
# print ("1. Took a cup")
# print ("2. poured coffee into the cup")
# print ("3. added sugar")
# print ("4. pour milk")
# print ("5. Stir")
# print ("6. ready to SERVE")

# num = input()

# using a function
def make_coffee():
    print ("1. Took a cup")
    print ("2. poured coffee into the cup")
    print ("3. added sugar")
    print ("4. pour milk")
    print ("5. Stir")

# using a function
def make_choose_coffee(choice1=None, choice2=None):
    print ("1. Took a cup")
    print ("2. poured coffee into the cup")
    print ("3. added sugar")
    print ("4. pour " + choice )
    print ("5. Stir")
    coffee = ''
    if choice1 == None:
        coffee = "Here is coffee with " + choice2
    elif choice2 == None:
        coffee = "Here is coffee with " + choice1
    elif choice1 == None and choice2 == None:
        coffee = "There is an error!!!"
    else:
        coffee = "Here is coffee with " + choice1 + " and " + choice2
    return coffee


# make_coffee()

def serve_coffee(name):
    coffe_made = make_coffee()
    print coffe_made
    # print (name + " " + coffe_made)


serve_coffee('Evance')
serve_coffee('Peter')
serve_coffee('Clemennt')