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

#complex wquation
eq1:complex = (2+3j)*(1+2j)
print(eq1)

###################### data types ended ##################################





# # split sentence and characters
# sentence = "We are learning Python"
# splitSentence = sentence.split()
# splitChars = list(sentence)
# print(splitSentence)
# print(splitChars)


# # counts the repeated alphabets in the given string
# fruit = "pomegranate"
# fruit.count("e")


# for multiple line statements, use triple quotes ("""   """)
# sentence = """We are
#     learning
# Python"""
# print(sentence)
