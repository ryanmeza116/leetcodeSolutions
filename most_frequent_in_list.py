# Given a list of numbers find which number occurrs most often in the list. Use a dict.
list = [1,6,5,44,5,78,77,77,5]
ans = 5

def find_most_frequent_number(numbers):
    frequency = {}
    max_frequency = 0
    most_frequent_number = None

    for number in numbers:
        print(f'Number currently is: {number}')
        if number in frequency:
            print(f'Number already in frequencey: {number}')
            frequency[number] += 1
            print(f'Frequency dict {frequency}')
            print(f'{frequency[number]}')
        else :
            frequency[number] = 1 #Adds element in list to dict, makes value 1
            print(f'current dict : {frequency}')
        if frequency[number] > max_frequency:
            max_frequency = frequency[number]
            most_frequent_number = number
    return most_frequent_number

print(find_most_frequent_number(list))

# When does the numbers in the list "numbers" get appended to the dictionary? 
# From line 17-29