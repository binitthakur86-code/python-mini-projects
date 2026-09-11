import random
import string


print("--- Strong Password Generator ---")
length = int(input("Length daalo (8-16): "))




password = [
     random.choice(string.ascii_uppercase),
     random.choice(string.digits),
     random.choice(string.punctuation)
]



all_chars = string.ascii_letters + string.digits + string.punctuation
for i in range(length - 3):
	password.append(random.choice(all_chars))
	
	
	
	
random.shuffle(password)


final_password = "".join(password)
print(f"\nFinalPassword: {final_password}")