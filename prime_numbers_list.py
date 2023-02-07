# def prime_numbers(n):
#     primes = []
#     for i in range (1, 20):
#         for j in range(2, int(n**0.5)+1):
#             if i % j == 0:
#                 break
#         else:
#             primes.append(i)
#     return primes

# prime_list = prime_numbers(20)
# print(prime_list)


lower = 1
upper = 20

print('Prime numbers between', lower, 'and', upper, 'are:')

for num in range (lower, upper + 1):
    if num > 1:
        for i in range (2, num):
            if (num % i) == 0:
                break
        else:
            print(num)