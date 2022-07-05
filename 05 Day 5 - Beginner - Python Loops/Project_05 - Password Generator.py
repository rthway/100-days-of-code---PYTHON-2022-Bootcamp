# Q.6 WAP to random generate password in python 
# Easy_level
import random
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','*']
nr_letters=int(input("how many letters would you like your password \n"))
nr_numbers=int(input("how many number would you like your password \n"))
nr_symbols=int(input("how many symbols would you like your password \n"))
password=""
for char in range (1,nr_letters+1):
  password += random.choice(letters)
for char in range (1,nr_numbers+1):
  password += random.choice(numbers)
for char in range (1,nr_symbols+1):
  password += random.choice(symbols)
print(f"Your password would be {password}")


#Hard level
import random
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','*']
nr_letters=int(input("how many letters would you like your password \n"))
nr_numbers=int(input("how many number would you like your password \n"))
nr_symbols=int(input("how many symbols would you like your password \n"))
password_list=[]
for char in range (1,nr_letters+1):
  password_list.append(random.choice(letters))
for char in range (1,nr_numbers+1):
  password_list.append(random.choice(numbers))
for char in range (1,nr_symbols+1):
  password_list.append(random.choice(symbols))

random.shuffle(password_list)

password=""
for char in password_list:
  password+=char
print(f"Your password would be {password}")