# Return function

# def f1(a, b, c):
#     return(a + b + c)
#
#
# result = f1(10, 20, 30)
# print(result)

# def print_argument(*args):  # *args allows you to pass any number of arguments
#     for i in args:
#         print(i, end="\n")


#print_argument(1, 2, 3, 4, 5)
# *args -> list

# a = ["promod", "amit", "ashish"]
# for i in a:
#     print(i)

def make_pizza(*topings):
    print(topings)
    for topin in topings:
        print(topin)


promod = make_pizza("tomato")
ashish = make_pizza("olives", "mushroom")
amit = make_pizza("corn", "onion", "capsicum")