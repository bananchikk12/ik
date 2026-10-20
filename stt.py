import random
import string

length = int(input("Введите длину пароля: "))
characters = string.ascii_letters + string.digits
password = ''.join(random.choice(characters) for _ in range(length))
print(password)