# SHA-224 Hash Function

## Properties

- **Digest Size:** 224 bits (28 bytes)
- **Block Size:** 512 bits (64 bytes)
- **Rounds:** 64

## Initialization

SHA-224 uses a set of constant initial values (also known as round constants) and an initial hash value (H0) as part of its initialization.

- Initial Hash Value (H0):
  - H0 = c1059ed8
  - H1 = 367cd507
  - H2 = 3070dd17
  - H3 = f70e5939
  - H4 = ffc00b31
  - H5 = 68581511
  - H6 = 64f98fa7
  - H7 = befa4fa4

## Round Constants

SHA-224 uses a set of constant round values (K) during each round of processing. These values are derived from the fractional parts of the cube roots of the first 64 prime numbers.

- Round Constants (K0 to K63):
  - K0 = 428a2f98
  - K1 = 71374491
  - K2 = b5c0fbcf
  - ...
  - K61 = a4506ceb 
  - K62 = bef9a3f7 
  - K63 = c67178f2

## Message Padding

Before processing the input message, SHA-224 pads it to a multiple of the block size (512 bits). The padding includes the original message length in bit-bytes.

## Round Function

During each round of processing, SHA-224 uses a set of logical functions and bitwise operations to update the hash value.

```python
def Right_Shift(x, y):
    return x >> y

def Rotate_Right(x, y):
    return (x >> y) | (x << (32 - y)) & 0xffffffff

def sigma0(x):
    return Rotate_Right(x, 7) ^ Rotate_Right(x, 18) ^ Right_Shift(x, 3)

def sigma1(x):
    return Rotate_Right(x, 17) ^ Rotate_Right(x, 19) ^ Right_Shift(x, 10)

def Ch(x, y, z):
    return (x & y) ^ (~x & z)

def Maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def Sigma0(x):
    return Rotate_Right(x, 2) ^ Rotate_Right(x, 13) ^ Rotate_Right(x, 22)

def Sigma1(x):
    return Rotate_Right(x, 6) ^ Rotate_Right(x, 11) ^ Rotate_Right(x, 25)
```

## Final Hash Value

The final hash value is the concatenation of the 8 32-bit words (H0 to H6) produced during the processing rounds.

## Example Usage

```python
from hashlib import sha224
from SHA224 import SHA224 as my_sha224


Message = b"This is a test for SHA-224 !!!"


my = my_sha224.sha224(Message)
hashlib = sha224(Message).hexdigest()

assert my == hashlib
print(f"Tryly {my} == {hashlib}")

```
```bash
Tryly c884cecaa6c1f5a316735b977806e4f21fe657d13a940c26a0a5392a == c884cecaa6c1f5a316735b977806e4f21fe657d13a940c26a0a5392a
```


