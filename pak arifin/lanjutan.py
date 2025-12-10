# 1. Konversi Tipe Data

# str ke int
str_numbers = "456"
str_numbers_to_int = int(str_numbers)
print("Before casting :", str_numbers, ", the data type is", type(str_numbers))
print("After casting :", str_numbers_to_int, ", the data type is", type(str_numbers_to_int))

# int ke str
integer = 12345
integer_to_str = str(integer)
print("Before casting :", integer, ", the data type is", type(integer))
print("After casting :", integer_to_str, ", the data type is", type(integer_to_str))

# int ke bool
num_int = 1
num_bool = bool(num_int)
print(num_bool, type(num_bool))

num_int = 0
num_bool = bool(num_int)
print(num_bool, type(num_bool))

# 2. Operator Perbandingan

print(8 == 8)   # Equal to
print(8 != 9)   # Not equal to
print(8 > 9)    # Greater than
print(8 < 9)    # Less than
print(8 <= 9)   # Less than or equal to
print(9 >= 9)   # Greater than or equal to

# 3. Operator Logika

a = True
b = True
print(a and b)
print(a or b)
print(not b)

# Gabungan logika
print(5 > 6 and 6 < 7)

# 4. Operator Aritmatika

e = 8
f = 2

sum = e + f
print(f"The sum of e with f is : {sum}")

red = e - f
print(f"The reduction of e with f is : {red}")

multi = e * f
print(f"The multiplication of e with f is : {multi}")

divi = e / f
print(f"The quotient of e with f is : {divi}")

mod = e % f
print(f"The remainder of e with f is : {mod}")

pow = e ** f
print(f"The power of e of f is : {pow}")

# 5. Input & Output

name = str(input("What is your name : "))
age = int(input("What's your age : "))
print("Name: ", name)
print("Age: ", age)

# Format output
print('Hi all! I am', name, 'age', age, 'years old')
print(f'Hi all! I am {name} age {age} years old')
print(f'Hi all! I am %s age %d years old' % (name, age))

# Dekorasi output
print(30 * "=")
print("Temperature Calculator Program")
print(30 * "=")


# 6. Conditionals & Exception Handling

# If-Else dengan try-except
try:
    your_GPA = float(input("Enter your GPA: "))
    if 4.0 >= your_GPA >= 0.0:
        if 4.0 >= your_GPA >= 3.80:
            print(f"Magna cumlaude! GPA: {your_GPA}")
        elif 3.50 <= your_GPA < 3.80:
            print(f"Cumlaude! GPA: {your_GPA}")
        elif 3.00 <= your_GPA < 3.50:
            print("GPA stabil")
        elif your_GPA < 3.0:
            print("Perlu perbaikan GPA")
    else:
        print("GPA di luar jangkauan")
except:
    print("Masukkan GPA yang valid")


# 7. Match Case (Python 3.10+)

try:
    status_code = int(input("Enter your status code: "))
    print("Your code means:")
    match status_code:
        case 200:
            print("Success!")
        case 400:
            print("Bad Request")
        case 401:
            print("Unauthorized")
        case 402:
            print("Payment Required")
        case 403:
            print("Forbidden")
        case 404:
            print("Not Found")
        case 500:
            print("Internal Server Error")
except:
    print("Masukkan kode status yang valid")



# 8. Kondisi Singkat

a = 3
b = "Even Numbers" if a % 2 == 0 else "Odd Numbers"
print(b)



# 9. Perulangan

# For loop biasa
for i in range(5):
    print(i)

# For loop dengan teks
for i in range(5):
    print("Data science is easy!")

# For loop dengan langkah
for i in range(1, 5, 2):
    print("Data science is easy!")

# Looping string
word = "I want to master data science"
for letter in word:
    print(letter)

# Looping dengan indeks
for m, n in enumerate(word):
    print(f"Index {m}. {n}")

# Loop mundur
for i in range(5, 1, -1):
    print("I want big data's")


# 10. continue & break

for i in range(5):
    if i == 2:
        continue  # skip saat i = 2
    if i == 4:
        break     # berhenti saat i = 4
    print(i)


# 11. While Loop

count = 0
while count < 4:
    print("Keep the spirits up interns!")
    count += 1