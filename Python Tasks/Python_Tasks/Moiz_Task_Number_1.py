# -----------------------------------
# Author: KHAWAJA ABDUL MOIZ
# Roll Number: 70288
# Email: khawajaahmedraza4@gmail.com
# ------------------------------------


#    Task 1:
# Q1) Even or Odd Checker:
#    Write a Python program that takes an integer input from the user and checks if it's even
#    or odd. Display an appropriate message.

EO=("Even or Odd Checker\n")
print(EO.center(70))
num = int(input("Enter an integer: "))  # Taking input from the user

if (num % 2) == 0:
    print(f"{num} is Even")  # If the remainder is 0, the number is even
else:
    print(f"{num} is Odd")  # Otherwise, the number is odd


#    Task 2:
# # Q2) Multiplication Table Generator:
# #    Create a program that generates a multiplication table for a given number. Allow the
# #    user to input the number and display the table.
    

#  Program to generate a multiplication table for a given number

# Ask the user to input the number for which the multiplication table is to be generated

MTG="Welcome to Multiplication Table Generator\n"
print(MTG.center(70))

num = int(input("Enter the number to generate its multiplication table: "))

# Define the range of the multiplication table, typically from 1 to 10
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")


#    Task 3:
# # Q3). Factorial Calculator:
# #    Write a Python program that calculates the factorial of a given number. Use a loop to
# #    perform the calculation.
    


FC="Factorial Calculator\n"
print(FC.center(70))

num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):  # Loop from 1 to the input number
    factorial *= i  # Multiply factorial by the current number
print(f"The factorial of {num} is {factorial}.")


#    Task 4:
# # Q4) Sum of Digits:
# #      Create a program that calculates the sum of the digits of a given number. For example, if
# #      the input is 12345, the output should be 15.



Sum="  Sum of Digits\n"
print(Sum.center(70))

num = input("Enter a number: ")
sum_digits = sum(int(digit) for digit in num)  # Sum the digits of the number
print(f"The sum of the digits is {sum_digits}.")




#    Task 5:
# # Q5) FizzBuzz Game:
# #    Implement the FizzBuzz game in Python. Write a program that prints the numbers from
# #    1 to 100. For multiples of 3, print "Fizz," for multiples of 5, print "Buzz," and for
# #    multiples of both 3 and 5, print "FizzBuzz."

FBG=" Welcome To FizzBuzz Game\n"
print(FBG.center(70))

num="Enter an Integer No"

for i in range(1, 101):  # Loop from 1 to 100
    if i % 3 == 0 and i % 5 == 0:  # Check if the number is divisible by both 3 and 5
        print("FizzBuzz")
    elif i % 3 == 0:  # Check if the number is divisible by 3
        print("Fizz")
    elif i % 5 == 0:  # Check if the number is divisible by 5
        print("Buzz")
    else:
        print(i)




#    Task 6:
# # Q6) Palindrome Checker:
# #    Develop a Python program that checks if a given word or phrase is a palindrome (reads
# #    the same forwards and backwards).

Pa=" Palindrome Checker\n"
print(Pa.center(70))

word = input("Enter a word or phrase: ").lower().replace(" ", "")  # Convert to lowercase and remove spaces
if word == word[::-1]:  # Check if the word is the same forwards and backwards
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")



#    Task 7:
# Q7) Prime Number Checker:
#    Write a program that checks if a given number is prime or not. Display an appropriate
#    message.
    
P="Prime Number Checker\n"
print(P.center(70))

num = int(input("Enter a number: "))
if num > 1:  # Check if the number is greater than 1
    for i in range(2, num):  # Loop from 2 to the number - 1
        if num % i == 0:  # Check if the number is divisible by any number other than 1 and itself
            print(f"{num} is not a prime number.")
            break  # Exit the loop if a divisor is found
    else:  # This else corresponds to the for loop
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


#    Task 8:
# Q8)Guess the Word Game:
#    Create a word guessing game where the computer selects a random word from a
#    predefined list, and the player has to guess the word one letter at a time.


G="Guess the Word Game\n"
print(G.center(70))

import random

words = ['python', 'programming', 'assignment', 'loops', 'conditions']
selected_word = random.choice(words)  # Select a random word from the list
guessed_word = ['_' for _ in selected_word]  # Create a list of underscores representing the word
attempts = len(selected_word) + 3  # Set the number of attempts

while attempts > 0 and '_' in guessed_word:  # Loop until all letters are guessed or attempts run out
    print(' '.join(guessed_word))
    guess = input("Guess a letter: ").lower()
    if guess in selected_word:  # Check if the guessed letter is in the word
        for i in range(len(selected_word)):
            if selected_word[i] == guess:
                guessed_word[i] = guess  # Reveal the letter in the guessed word
    else:
        print("Incorrect guess.")
    attempts -= 1  # Decrement the number of attempts

if '_' not in guessed_word:  # Check if all letters have been guessed
    print(f"Congratulations! The word was '{selected_word}'.")
else:
    print(f"Sorry, you ran out of attempts. The word was '{selected_word}'.")








