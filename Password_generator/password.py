#collect user preference 
#length
#should contain uppercase
#should contain digits
#should contain special digits
#get all avaliable characters
#randomly pick characters upto the length
#ensure we have least one character type 
#ensure length is valid 

import string
import random
from tokenize import Special

def generate_password():
  length = int(input("Enter desired length password: ").strip())
  include_uppercase = input("Include uppercase characters only (yes/no)").strip().lower()
  include_digits = input("Include digits? (yes/no)").strip().lower()
  include_special_characters = input("Include special characters? (yes/no)").strip().lower()

  if length < 4:
    print("length must be atleast 4")
    return
 
  lower = string.ascii_lowercase
  upper_Case = string.ascii_uppercase if include_uppercase == "yes" else ""
  special = string.punctuation if include_special_characters == "yes" else ""
  digits = string.digits if include_digits == "yes" else ""
  all_characters = lower + upper_Case + special + digits
  # print(all_characters)

  required_pass = []

  if include_uppercase == "yes":
    required_pass.append(random.choice(upper_Case))
  if include_digits == "yes":
    required_pass.append(random.choice(digits))
  if include_special_characters == "yes":
    required_pass.append(random.choice(special))

  remaining_len = length - len(required_pass)
  password = required_pass

  for _ in range(remaining_len):
    character = random.choice(all_characters)
    password.append(character)
    
  random.shuffle(password)

  str_password = "".join(password)
  return str_password


password = generate_password()
print(password)






