# Consider a list in python, there are 7 total commands which can be preformed. 
# Insert integer e at position i, print list, remove e, append e, sort, pop, and reverse. 
# Initialize your list and read in the value of n followed by n lines of commands where each command will be on the 7 types listed. 
# Iterate through each command in order and preform the corresponding operation on your list. 

# Solution: 

# Initialize an empty list
my_list = []

# Read the value of n
n = int(input())

# Iterate through each command
for _ in range(n):
    command = input().split()
    operation = command[0]

    if operation == "insert":
        # Insert integer e at position i
        i = int(command[1])
        e = int(command[2])
        my_list.insert(i, e)
    elif operation == "print":
        # Print the list
        print(my_list)
    elif operation == "remove":
        # Remove element e from the list
        e = int(command[1])
        my_list.remove(e)
    elif operation == "append":
        # Append element e to the list
        e = int(command[1])
        my_list.append(e)
    elif operation == "sort":
        # Sort the list in ascending order
        my_list.sort()
    elif operation == "pop":
        # Remove and return the last element from the list
        my_list.pop()
    elif operation == "reverse":
        # Reverse the elements in the list
        my_list.reverse()
