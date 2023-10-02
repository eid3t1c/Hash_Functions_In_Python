# SHA-256 Hash Function

## Properties

- **Digest Size:** 256 bits (32 bytes)
- **Block Size:** 512 bits (64 bytes)
- **Rounds:** 64

## Initialization

SHA-256 uses a set of constant initial values (also known as round constants) and an initial hash value (H0) as part of its initialization.

- Initial Hash Value (H0):
  - H0 = 6a09e667
  - H1 = bb67ae85
  - H2 = 3c6ef372
  - H3 = a54ff53a
  - H4 = 510e527f
  - H5 = 9b05688c
  - H6 = 1f83d9ab
  - H7 = 5be0cd19

## Round Constants

SHA-256 uses a set of constant round values (K) during each round of processing. These values are derived from the fractional parts of the cube roots of the first 64 prime numbers.

- Round Constants (K0 to K63):
  - K0 = 428a2f98
  - K1 = 71374491
  - K2 = b5c0fbcf
  - ...
  - K61 = a4506ceb 
  - K62 = bef9a3f7 
  - K63 = c67178f2

## Message Padding

Before processing the input message, SHA-256 pads it to a multiple of the block size (512 bits). The padding includes the original message length in bit-bytes.

## Round Function

During each round of processing, SHA-256 uses a set of logical functions and bitwise operations to update the hash value.
```python
def Right_Shift(x,y):
    return x >> y

def Rotate_Right(x,y):
    return (x >> y) | (x << (32 - y)) & 0xffffffff

def sigma0(x):
    return Rotate_Right(x,7) ^ Rotate_Right(x,18) ^ Right_Shift(x,3)

def sigma1(x):
    return Rotate_Right(x,17) ^ Rotate_Right(x,19) ^ Right_Shift(x,10)

def Ch(x,y,z):
    return (x & y) ^ (~x & z)

def Maj(x,y,z):
    return (x & y) ^ (x & z) ^ (y & z)

def Sigma0(x):
    return Rotate_Right(x,2) ^ Rotate_Right(x,13) ^ Rotate_Right(x,22)

def Sigma1(x):
    return Rotate_Right(x,6) ^ Rotate_Right(x,11) ^ Rotate_Right(x,25)
```
## Final Hash Value

The final hash value is the concatenation of the 8 32-bit words (H0 to H7) produced during the processing rounds.

## Example Usage

```python
from hashlib import sha256
from SHA256 import SHA256 as my_sha256


Message = b"This is a test for SHA-256 !!!"


my = my_sha256.sha256(Message)
hashlib = sha256(Message).hexdigest()

assert my == hashlib
print(f"Tryly {my} == {hashlib}")
```
```bash
Truly 46308f374b2f8f5f21fa7399dd350b4c337e03cea357fadf6e5c12d21339014c == 46308f374b2f8f5f21fa7399dd350b4c337e03cea357fadf6e5c12d21339014c
```


