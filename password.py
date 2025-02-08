import random

#input
length = input("Insertar un número entero positivo: ")

try:
  length = int(length)
  #generator
  def create_password(pass_length):
    typing= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

  for i in range(pass_length):
    password += random.choice(typing)
    return print(password)
  create_password(length)
except ValueError: 
  print("No puedo usar ese número.")

#Usando try en vez de if
