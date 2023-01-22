import sqlite3 as db

# connect to database file to store already searched numbers, create the file if it doesn't exist
con = db.connect('Searched_numbers.db')

# cursor for executing SQL queries
c = con.cursor()

# Create table factors if it doesn't exist already
c.execute("""CREATE TABLE IF NOT EXISTS factors (
            number integer,
            factors text
 )""")

#table = c.execute("""SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE factors""")
#print(table)

print("With this program you can calculate the prime factors of any given number")


# Store user input in a variable
user_number = int(input("Give me number:"))

# Functionality here to check database for existing numbers

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

# write prime factores to database file

print(prime_list_output)



