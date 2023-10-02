# SHA-384 Hash Function

## Properties

- **Digest Size:** 384 bits (48 bytes)
- **Block Size:** 1024 bits (128 bytes)
- **Rounds:** 80

## Initialization

SHA-384 uses a set of constant initial values (also known as round constants) and an initial hash value (H0) as part of its initialization.

- Initial Hash Value (H0 to H7):
  - H0 = cbbb9d5dc1059ed8
  - H1 = 629a292a367cd507
  - H2 = 9159015a3070dd17
  - H3 = 152fecd8f70e5939
  - H4 = 67332667ffc00b31
  - H5 = 8eb44a8768581511
  - H6 = db0c2e0d64f98fa7
  - H7 = 47b5481dbefa4fa4

## Round Constants

SHA-384 uses a set of constant round values (K) during each round of processing. These values are derived from the fractional parts of the cube roots of the first 80 prime numbers.

- Round Constants (K0 to K79):
  - K0 = 428a2f98d728ae22
  - K1 = 7137449123ef65cd
  - K2 = b5c0fbcfec4d3b2f
  - ...
  - K77 = 597f299cfc657e2a
  - K78 = 5fcb6fab3ad6faec
  - K79 = 6c44198c4a475817

## Message Padding

Before processing the input message, SHA-384 pads it to a multiple of the block size (1024 bits). The padding includes the original message length in bit-bytes.

## Round Function

During each round of processing, SHA-384 uses a set of logical functions and bitwise operations to update the hash value.

```python
def Right_Shift(x, y):
    return x >> y

def Rotate_Right(x, y):
    return (x >> y) | (x << (64 - y)) & 0xffffffffffffffff

def sigma0(x):
    return Rotate_Right(x, 28) ^ Rotate_Right(x, 34) ^ Rotate_Right(x, 39)

def sigma1(x):
    return Rotate_Right(x, 14) ^ Rotate_Right(x, 18) ^ Rotate_Right(x, 41)

def Ch(x, y, z):
    return (x & y) ^ (~x & z)

def Maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def Sigma0(x):
    return Rotate_Right(x, 1) ^ Rotate_Right(x, 8) ^ Right_Shift(x, 7)

def Sigma1(x):
    return Rotate_Right(x, 19) ^ Rotate_Right(x, 61) ^ Right_Shift(x, 6)
```
## Final Hash Value

The final hash value is the concatenation of the 6 64-bit words (H0 to H5) produced during the processing rounds.


## Example Usage

```python
from hashlib import sha384
from SHA384 import SHA384 as my_sha384


Message = b"This is a test for SHA-384 !!!"


my = my_sha384.sha384(Message)
hashlib = sha384(Message).hexdigest()

assert my == hashlib
print(f"Tryly {my} == {hashlib}")

```
```bash
Tryly 186a0b005d6649c6634fdfa03a4d98a4f333f714138a9b83908672e890fc93b70b64cf168ab88407a475c21d5c1ea7a5 == 186a0b005d6649c6634fdfa03a4d98a4f333f714138a9b83908672e890fc93b70b64cf168ab88407a475c21d5c1ea7a5
```
