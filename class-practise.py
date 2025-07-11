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

# # LOOP
# for i in range(0, 10):
#     print(i)


# # TUPLE (unchangeable)
# myTuple: tuple = (3, 5, "Testing", [2, 3, 4, 5], False)
# print(f"\n\n{myTuple}")

# # we can create copy of array so that it does not affect its original array
# makeCopy = myTuple[3].copy()
# makeCopy[1] = 55
# print(makeCopy)
# print(myTuple)

# arr = myTuple[3]  # updating couple's array element by hack
# arr[1] = 55
# print(arr)
# print(myTuple)  # tuple updated because of memory reference


# # DICTIONARY
# myDict: dict = {
#     "name": "Saim",
#     "age": 23,
#     "rollNo": 2327,
# }
# print(f"\n\n{myDict}")
# print(myDict["age"])


# # TypeCasting
# i: int = 32
# print("\n\nValue of i = ", str(i))
# print("Type of i = ", str(type(i)))


# a: int = -10
# b: bool = bool(a)
# print("\n\nValue of b = ", str(b))  # "True"  value of string
# print("Type of b = ", str(type(b)))


# # check instance
# num: float = 77, 543.545
# print(f"\n\n{isinstance(num, int)}")


# myList: list[int] = [32, 43, 11, 2, 6]
# print("7 in my list: ", 7 in myList)
# print("10 is not in my list: ", 10 not in myList)


# # join method
# sentenceList: list = ["Python", "Programming"]
# joinSentence: str = " ".join(sentenceList)
# print(joinSentence)

# fruit: str = "Apple" * 3  # multiplying string
# print(fruit)


# # reference understanding
# std: object = {
#     "name": "Ali",
#     "age": 14,
# }  # this will be updated because it is passed refernce
# std1 = std
# std1["name"] = (
#     "Shakir"  # both std and std1 will be updated because of reference sharing
# )
# print(std)
# print(std1)

# name: str = "Ali"
# name1 = name
# print(name)
# print(name1)
# name1 = "Shakir"
# print(name1)
# print(name)  # the name value still hold Ali because it is passed by value
"""these are immutable data types: string,int,float,complex; because they are passed by value"""
"""these are mutable data types: list, dictionary, sets; becaise they are passed by value"""


# # SET  (only unique elements), set is unchangeable but mutable, means that we cannot update its current value but we can add new value in it
# mySet: set = {3, 4, 2, "2", 3}
# print(f"\n\n{mySet}")
# mySet.add(18)  # adds only one element at a time
# print(mySet)
# mySet.update(["Testing", 434])  # can add more than one element
# print(mySet)
# mySet.remove("Testing")  # removes single element but if not found, throws an error
# print(mySet)
# mySet.discard("2")  # removes single element but if not found, nothing will happen

# # frozen set (immutable):: we cannot add or remove element from that
# fSet: frozenset = frozenset([1, 2, 3, 433, 3, "Ali"])
# print(fSet)


# # positionl only arguments(once declare all params, then give, then /)
# def posFun(a, c, d, /, b):
#     print(f"these are positional arguments: {a}, {c}, {d}")
#     print(f"this is a keyword argument: {b}")


# posFun(4, 2, 3, b=7)


# # EXCEPTION HANDLING

# def exception_handling():
#     while True:
#         try:
#             num: int = int(input("Enter any integer number:\t"))
#         except ValueError as e:
#             print(f"Invalid value: {e}")
#         except Exception as e:  # when we don't know which type of error can occured
#             print(f"An Unexpected error occured: {e}")
#         else:
#             print(
#                 f"{num}No error were raised"
#             )  # the else will run when try has no error and successfully executes
#             break
#         finally:
#             print("I will always run no matter what")
#     return num


# get_num = exception_handling()
# print(f"Number after handling exception is {get_num}")

