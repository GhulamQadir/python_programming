#######################            DATA TYPES   ##############################3
# # variable with type hinting is preferred(anytime we can assign different typed value in it nut not preferred)
# charges: int = 30000
# print(charges)
# a = 70
# a = "340"
# print(a + charges)  # it will give error


# # type casting(its hinting not type annotation)
# val: int = 67.40076
# print(type(val), "val_int: ", val) # it just hints that we should assign int type to it but not annotate


# # complex number
# numComplex: complex = 4 + 5j  # j is the sq.root of -1 (it's actually i)
# ### real part is mandatory in imaginary like imaginary is never stand alone (j should be assign with any number)
# print(numComplex)

# #complex equation
# eq1:complex = (2+3j)*(1+2j)
# print(eq1)


# numRange: range = range(3, 15, 3)
# print(numRange)

###################### data types ended ##################################

# # mutiple line comment
# """We are
# learning
#     pyhon
# """

# # double quote (multi text) does not work
# a: str = "We are " "learning " "Python!"
# print(a)

# b: str = """We are
#     learning
#         Python"""
# print(b)


# for i in range(0, 10):
#     print(i)


# SET
mySet: set = {3, 4, 2, "2", 3}
print(mySet)
mySet.add(18)
print(mySet)

# frozen set (immutable)
fSet: frozenset = frozenset([1, 2, 3, 433, 3, "Ali"])
print(fSet)
