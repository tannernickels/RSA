import random as rand
def gcd(a, b):
  if b==0:
    return a
  else:
    return gcd(b, a%b)

def sieve():
  n = 1000
  nums = ["p" for x in range(n)]
  nums[0] = 0
  nums[1] = 1
  for i in range(len(nums)):
    if nums[i]=='p':
      for j in range(i+1, len(nums)):
        if j%i==0:
          nums[j]='c'
  random_prime = rand.randint(2, n-1)
  while nums[random_prime]!='p':
    random_prime = rand.randint(2, n-1)
  return random_prime

def choose_e(phi):
  rand_e = rand.randint(3, 1000)
  while gcd(phi, rand_e) != 1:
    rand_e = rand.randint(3, 1000)
  return rand_e

def getInverse(a, m):
  m0 = m
  y = 0
  x=1

  if m==1:
    return 0

  while a>1:

    q = int(a/m)
    t = m

    m = a%m
    a = t
    t = y
    y = x - q*y
    x = t
  
  if x<0:
    x += m0
  
  return x

def createKeypair():
  p = sieve()
  q = sieve()
  N = p*q
  phi = (p-1)*(q-1)
  e = choose_e(phi)
  d = getInverse(e, phi)

  return (N, e), (N, d)

def encrypt(plaintext, public_key):
  ciphertext = ''
  N, e = public_key[0], public_key[1]
  for char in plaintext:
    num = ord(char)
    encrypted_char = (num**e)%N 
    ciphertext += chr(encrypted_char)
  return ciphertext

def decrypt(ciphertext, private_key):
  plaintext = ''
  N, d = private_key[0], private_key[1]
  for char in ciphertext:
    num = ord(char)
    decrypted_char = (num**d)%N
    plaintext += chr(decrypted_char)
  return plaintext

public, private = createKeypair()

message = "Hello!"
print(message)
encrypted = encrypt(message, public)
print(encrypted)
decrypted = decrypt(encrypted, private)
print(decrypted)
