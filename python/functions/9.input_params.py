chai = "Ginger chai"

def prepare_chai(order):
    print("Preparing ", order)

prepare_chai(chai)
print(chai)

# another example
chai_cups = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai_cups)
print(chai_cups)

# another example
def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") # positional
make_chai(milk="No", sugar="Medium", tea="Oolong") #keywords


#another example
def special_chai(*ingredients, **extras): # *args, **kwargs
    print("Ingredients: ", ingredients)
    print("Extras: ", extras)

special_chai("Cinnamon", "Cardemom", sweeteners="Honey", foam="Yes")

#another example

# def chai_order(order=[]):
#    order.append("Masala")
#    print(order)

def chai_order(order=None):
    if order is None:
        order=[]
    print(order)

chai_order()
chai_order()

