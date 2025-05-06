#Write a python program using For Loop to iterate through a list of colors and prints each color.

# colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white", "gray", "cyan", "magenta"]
# for color in colors:
#     print(color)

#WHILE LOOP
# Write a short guessing game program using a while loop. The 
# user should be prompted to guess a number, and you should tell 
# them whether their guess was correct or wrong after each 
# guess. The loop should keeping running until the user guesses 
# the number correctly


# secret_number = 7
# guess = None

# while guess != secret_number:
#     guess = int(input("Guess a number: "))
#     if guess == secret_number:
#         print("Correct! Lucky this round.")
#     else:
#         print("Wrong! Unlucky this round.")    



# Write a short guessing game program using a while loop. The 
# user should be prompted to guess a number between 1 and 100, 
# and you should tell them whether their guess was too high or 
# too low after each guess. The loop should keeping running until 
# the user guesses the number correctly.






# guess_number = 56
# guess = None

# while guess != guess_number:
#     guess = int(input("Guess a number between 1 and 100: "))
#     if guess>guess_number:
#         print("The number is too large")
#     elif guess<guess_number:
#         print("The number is too small")
#     else:
#         print("You guessed correctly")  






# Write  a  Python  Program  using  While  Loop  that  calculates  the 
# sum of numbers from 1 to 500.          

# number = 1
# total = 0

# while number <= 500:
#     total +=number
#     number +=1

# print("The sum of numbers from 1 to 500 is:", total)



# Write a python program using while loop that counts down from 
# 5 to 1.

# count = 5

# while count >=1:
#     print(count)
#     count -=1





# Write  a  python  program  using  while  loop  to  print  all  even 
# numbers between 1 and 50.



# i = 1

# while i in range(50):
#     if i % 2 !=0:
#         i +=1
#         continue
#     print(i)
#     i +=1





# Write a python program using while loop that prints a triangle 
# pattern of stars.



# rows = 5 
# i = 1

# while i <= rows:
#     print("*" * i)
#     i+=1




#NESTED LOOPS

# Write a python program using nested loops to print a right angled triangle using stars.

# rows = 5

# for x in range(1, rows + 1):
#     for j in range(x):
#          print("*", end="")
#     print()     




# Create a Python program using nested loops  prints a pattern where each row 
# has the same number repeated.



# for i in range(1, 6):
#     for j in range(i):
#         print(i, end='')
#     print()
