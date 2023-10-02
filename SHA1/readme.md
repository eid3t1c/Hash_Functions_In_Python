# SHA-1 Hash Function

## Properties

- **Digest Size:** 160 bits (20 bytes)
- **Block Size:** 512 bits (64 bytes)
- **Rounds:** 80

## Initialization

SHA-1 uses a set of constant initial values (also known as round constants) and an initial hash value (H0) as part of its initialization.

- Initial Hash Value (H0 to H4):
  - H0 = 67452301
  - H1 = EFCDAB89
  - H2 = 98BADCFE
  - H3 = 10325476
  - H4 = C3D2E1F0

## Constants

SHA-1 uses a set of constant values (K) during each round of processing. These values are as follows:

- K0 to K19: 0x5A827999
- K20 to K39: 0x6ED9EBA1
- K40 to K59: 0x8F1BBCDC
- K60 to K79: 0xCA62C1D6

## Message Padding

Before processing the input message, SHA-1 pads it to a multiple of the block size (512 bits). The padding includes the original message length in bits.

## Round Function

During each round of processing, SHA-1 uses a set of logical functions and bitwise operations to update the hash value.

```python
def Ch(x,y,z):
    return (x & y) ^ (~x & z)

def Maj(x,y,z):
    return (x & y) ^ (x & z) ^ (y & z)

def Parity(x,y,z):
    return x ^ y ^ z

def Rotate_Left(x,y):
    return ((x << y) | (x >> (32-y))) & 0xFFFFFFFF
```

## Final Hash Value

The final hash value is the concatenation of the 5 32-bit words (H0 to H4) produced during the processing rounds.

## Example Usage

```python
from hashlib import sha1
from SHA1 import SHA1 as my_sha1


Message = b"This is a test for SHA-1 !!!"


my = my_sha1.sha1(Message)
hashlib = sha1(Message).hexdigest()

assert my == hashlib
print(f"Tryly {my} == {hashlib}")

```
```bash
Tryly d2a3aa74e1078766505d3e70b75ec34d94b15fd0 == d2a3aa74e1078766505d3e70b75ec34d94b15fd0
```
