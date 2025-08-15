import random
import string
len_password=int(input("enter the lenght of your password(atleast 6):"))
if len_password<6:
    raise ValueError("Password length should be at least 6 characters.")
print("we all know that password is a combination of upper_case ,lowerc_case,\n special symbol and different number:")
password_char=[]


# generate uppercase character and append to the password char

for i in range(len_password * 30 // 100):
    upper_case=random.choice(string.ascii_uppercase)
    print("Uppercase letter:",upper_case)
    password_char.append(upper_case)


# generate lowercase character

for i in range(len_password * 30 // 100):
    lower_case=random.choice(string.ascii_lowercase)
    print("lowercase character:",lower_case)
    password_char.append(lower_case)



# generate number

for i in range(len_password * 20 // 100):
    number=str(random.randint(0,9))
    print("number:",number)
    password_char.append(number)


# generate special symbol

special_list=["@","#",'$','%','^','&','*','_']
for i in range(len_password-((len_password * 30 // 100)+(len_password * 30 // 100)+(len_password * 20 // 100))):
    special_symbol=random.choice(special_list)
    print("special symbol:",special_symbol)
    password_char.append(special_symbol)

# show list
print("your password symbol:",password_char)

# Shuffle characters
random.shuffle(password_char)

# Join characters to form the password
password = ''.join(password_char)
print("\nYour generated password:", password)