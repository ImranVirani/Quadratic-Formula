# Purpose: This program is intended to evaluate the quadratic formula mutiple
# times if specified by the user, the values of a, b, and c from the standard
# form of a quadratic equation and the discriminant and soltutions are given
# Status: Work in Progress
# Author: Imran Virani

# Library used for square rooting the discriminant in the quadratic equation
import math
# Opening Statement
print("Welcome to the quadratic formula calculator!")
print()
numOfEqations = eval(
    input("Please enter the number of equations that will be solved: "))
while type(numOfEqations) != eval and type(numOfEqations) != int:
    print("The number of equations entered is invalid as you must enter a whole number greater than 0, please try again.")
    numOfEqations = eval(
        input("Please enter the number of equations that will be solved: "))
    print()
while (numOfEqations == 0) or (numOfEqations < 0):
    print("The number of equations you wish to solve is invalid as the you cannot solve",
          numOfEqations, "equations", "please try again")
    print()
    numOfEqations = eval(
        input("Please enter the number of equations that will be solved: "))
    print()
counter = 1
equationNumberCounter = counter
# Iterates based on the number of equations to be evaluated
while counter <= numOfEqations:
    # The user inputs the values of a, b, and c
    a = eval(input("What is the coefficient of a (as a number) in quadratic equation number " +
                   str(equationNumberCounter) + " in the standard form y=ax\u00B2+bx+c: "))
    # Makes sure that the a value inputted is a number
    while type(a) == str:
        print(
            "The input entered is invalid because you entered a string please try again")
        print()
        a = eval(input("What is the value of a (as a number) in quadratic equation number " + str(equationNumberequationNumberCounter)
                       + " from the standard form y=ax\u00B2+ bx + c: "))
    while a == 0:
        print(
            "The input entered is invalid because you entered 0 which caused x\u00B2 to be 0 which makes the equation not a quadratic please try again")
        print()
        a = eval(input("What is the value of a (as a number) in quadratic equation number " +
                       str(equationNumberCounter) + " from the standard form y=ax\u00B2+bx+c: "))
    print("The value of a is", a)
    print()
    b = eval(input("What is the coefficient of b (as a number) in quadratic equation number " +
                   str(equationNumberCounter) + " from the standard form y=ax\u00B2+bx+c: "))
    # Makes sure that the b value inputted is a number and not a string
    while type(b) == str:
        print()
        print("The input entered is invalid please try again")
        b = eval(input("What is coefficient of b (as a number) in the quadratic equation number " +
                       str(equationNumberCounter) + " from the standard form y=ax\u00B2 + bx +c: "))
    print("The value of b is", b)
    print()
    c = eval(input("What is the value of c, the constant (as a number) in quadratic equation number " +
                   str(equationNumberCounter) + " from the standard form y=ax\u00B2+bx+c: "))
    # Makes sure the c value inputted is a number
    while type(c) == str:
        print("The input entered is invalid please try again")
        print()
        c = eval(input("What is the value of c (as a number), the contant in quadratic equation number" +
                       str(equationNumberCounter) + " from the standard form y=ax\u00B2+bx+c: "))
    print("The value of c is", c)
    print()
    output = "The Quadratic equation for equation number " + str(equationNumberCounter) + " for the values entered is y = " + \
        str(a) + "x\u00B2" + "+" + str(b) + "x" + "+" + str(c)
    if "1x" in output:
        output = output.replace("1x", "x")
    if "+-" in output:
        output = output.replace("+-", "-")
    if "+0x" in output:
        output = output.replace("+0x", "")
    if "+0" in output:
        output = output.replace("+0", "")
    if "-0" in output:
        output = output.replace("-0", "")
    if "+x" in output:
        output = output.replace("+0x", "")
    print(output)

    # The discriminant, b^2-4ac is evaluated and stored so that it can be used later
    discriminant = (b ** 2) - (4 * a * c)
    print("The discriminant is", discriminant)
    # The laws that apply to the discriminant, namely if D < 0 there are no
    # solutions, if D > 0, there are two solutions and if D is equal to 0 there is one solution
    # Checks if the discriminant is less than zero
    if (discriminant < 0):
        print("Because the discriminant(b\u00B2-4ac),", discriminant,
              "is less than 0, there are no solutions")
        print()
    else:
        # Checks if the discriminant is zero
        if discriminant == 0:
            print("Because the discriminant equals 0, there is one solution")
            print()
            solution1 = (-1 * b) / (2 * a)
            # Because there is only one solution per the discriminant,
            # only one solution needs to be printed
            print(
                "Because the discriminant is 0 there is only one solution which is x =", solution1)
        else:
            # The final case is that there are two real disctint solutions,
            # when the discriminant is greater than 0
            print("Because the discriminant equals", str(
                discriminant) + ", there are two solutions")
            print()
            solution1 = ((-1 * b) + (math.sqrt(discriminant))) / (2 * a)
            solution2 = ((-1 * b) - (math.sqrt(discriminant))) / (2 * a)
            if solution2 == -0:
                solution2 = 0
            print("The two solutions are x =",
                  solution1, "and", "x =", solution2)
            print()
    counter = counter + 1
    equationNumberCounter = equationNumberCounter + 1
print("All quadratic equations have been solved")
# Confirms exit
quit = input("To quit the program please enter 'exit' or 'quit': ")
while quit != "quit" and quit != "exit":
    quit = input("To quit the program please enter 'exit' or 'quit': ")
    print("Sorry your input", quit, "was invalid")
print("")
# Closing Statement
print("Thank you for using the quadratic formuala calculator!")
