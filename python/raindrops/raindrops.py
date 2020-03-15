# Iteration 1
# def convert(number):
#     if number % 105 == 0:
#         return "PlingPlangPlong"
#     elif number % 35 == 0:
#         return "PlangPlong"
#     elif number % 21 == 0:
#         return "PlingPlong"
#     elif number % 15 == 0:
#         return "PlingPlang"
#     elif number % 7 == 0:
#         return "Plong"
#     elif number % 5 == 0:
#         return "Plang"
#     elif number % 3 == 0:
#         return "Pling"
#     else:
#         return str(number)


# # Iteration 2
# def convert(number):
#     s = ""
#     if number % 3 == 0:
#         s += "Pling"
#     if number % 5 == 0:
#         s += "Plang"
#     if number % 7 == 0:
#         s += "Plong"
#     return s if s else f"{number}"

# Iteration 3
# makes the code more concise and extensible
# easier to add extra factors later
def convert(number):
    s = ""
    factors = [3, 5, 7]
    names = ["Pling", "Plang", "Plong"]

    for index, f in enumerate(factors):
        if number % f == 0:
            s += names[index]
    
    return s if s else f"{number}"
