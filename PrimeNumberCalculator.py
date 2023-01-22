import sqlite3 as db

con = db.connect('Searched_numbers.db')

print("With this program you can calculate the prime factors of any given number")


# Store user input in a variable
user_number = int(input("Give me number:"))

# calculate prime factors of user given number
def calc_prime_fact(x):
    prime_factors = []
    i = 2
    while i <= x:
        if x%i == 0:
            prime_factors.append(i)
            x = x/i
        else:
            i += 1
    return prime_factors
    
# Store list of found prime factors in a variable
prime_list = calc_prime_fact(user_number)

# Remove duplicate entries from found prime factors list
def cut_duplicates(list):
    refined_list = []
    for i in list:
        if i not in refined_list:
            refined_list.append(i)
    return refined_list

# Store refined prime factor list with no double values in a variable
prime_list_output = cut_duplicates(prime_list)

# Create file here and write prime factores list in it

print(prime_list_output)



