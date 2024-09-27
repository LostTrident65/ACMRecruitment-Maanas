# Problem 1: The sum of all multiples of 3 or 5 below 1000.
sum = 0  
for i in range(1000):  
    if i % 3 == 0 or i % 5 == 0:  
        sum += i  

print("The sum of all multiples of 3 or 5 below 1000 is:", sum)


# Problem 2: The sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million.
a, b = 1, 2  
sum = 0  

while a <= 4000000:  
    if a % 2 == 0:  
        sum += a  
    a, b = b, a + b  

print("The sum of the even-valued terms in the Fibonacci sequence not exceeding four million is:", sum)


# Problem 3: The largest prime factor of the number 600851475143.
def LargestPrime(n):  
    f = 2  
    while n > 1:  
        if n % f == 0:  
            n //= f  
        else:  
            f += 1  
    return f  

num= 600851475143  
LF = LargestPrime(num)  
print("The largest prime factor is:", LF)


# Problem 4: The largest palindrome made from the product of two 3-digit numbers.
def largest_palindrome():  
    MP = 0  
    for i in range(100, 1000):  
        for j in range(i, 1000):  
            P = i * j  
            if str(P) == str(P)[::-1] and P > MP:  
                MP = P  
    return MP  
  
print("The largest palindrome made from the product of two 3-digit numbers is:", largest_palindrome())


# Problem 7: The 10001st prime number.
def is_prime(n):  
    if n <= 1:  
        return False  
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:  
            return False  
    return True  

def nth_prime(n):  
    c = 0  
    num = 1  
    while c < n:  
        num += 1  
        if is_prime(num):  
            c += 1  
    return num  
 
print("The 10,001st prime number is:", nth_prime(10001))
