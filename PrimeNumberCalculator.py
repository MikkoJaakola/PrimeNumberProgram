print("With this program you can calculate the prime factors of any given number")


# Store user input in a variable
user_number = int(input("Give me number:"))

new_number = user_number + 69

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
    

print(calc_prime_fact(user_number))



