import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE `primenos`")
cursor.execute("USE `primenos`")
cursor.execute("""CREATE TABLE IF NOT EXISTS `prime_numbers`(
        `id` INT PRIMARY KEY AUTO_INCREMENT,
        `prime_number` INT NOT NULL
)""")


lower = 1
upper = 20

print('Prime numbers between', lower, 'and', upper, 'are:')

prime_numbers = []
for num in range (lower, upper + 1):
    if num > 1:
        for i in range (2, num):
            if (num % i) == 0:
                break
        else:
            #print(num)
            prime_numbers.append(num)

print(prime_numbers)
# cursor.execute("INSE")
connection.commit()

