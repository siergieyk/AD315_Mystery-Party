import numpy as np

primenums = []
for i in range(2, 103):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
    if prime:
        primenums.append(i)

alphabet = []

for i in range(97,123):
  alphabet.append(chr(i))
  


cipher = dict(zip(alphabet, primenums))

def saspc(word):
  import numpy
  
  li = list(word)
  
  nums = []
  
  
  for i in li:
    if i in cipher.keys():
      nums.append(cipher.get(i))
        
  print("\nYour code is:",numpy.prod(nums))


  
def dec2bin(num):
  number = int(num)
  i = 0
  bin = []
  while (number > 0):
    reminder = number % 2
    
    bin.append(str(reminder))
    number = number // 2

  print("Your decimal number:", num, " = ",''.join(bin[::-1]),"in binary")
