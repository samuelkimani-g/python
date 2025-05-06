# Write a function to find the largest number in a list

# a = [1,2,3,4,5,6,7,8,9,3]

# largest_number = max(a)
# print(largest_number)



# Create a list of characters. Write a program to reverse the order of the elements in the list 
# without using built-in functions. Use indexing method


# people = ["Mark", "Liam", "Stacy", "Sam", "Joy"]



#LIST COMPREHENSION
#TRADITONAL METHOD
# squres = []
# for elem in range (5):
#     squres.append(elem * elem)
    
# print(squres)    

#SIMPLE METHOD

squres = [elem * elem for elem in range (5)]
print(squres)

