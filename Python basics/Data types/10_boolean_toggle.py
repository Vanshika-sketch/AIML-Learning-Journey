# Program to take a boolean input and print its opposite value

value = input("Enter True or False: ")


if value == "True":
    boolean_value = True
else:
    boolean_value = False

opposite_value = not boolean_value

print("Original value:", boolean_value)
print("Opposite value:", opposite_value)
