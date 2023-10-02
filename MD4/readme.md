# MD4 (Message Digest 4) Hash Function

## Overview

- **Digest Size:** 128 bits (16 bytes)
- **Block Size:** 512 bits (64 bytes)

## Initialization

MD4 uses a set of constant initial values (also known as round constants) and an initial hash value (A, B, C, D) as part of its initialization.

- Initial Hash Value (A, B, C, D):
  - A = 0x67452301
  - B = 0xEFCDAB89
  - C = 0x98BADCFE
  - D = 0x10325476

## Constants

MD4 uses a set of constant values in its rounds.

- Constants (T):
  T[1] = 0x5A827999
  T[2] = 0x6ED9EBA1

## Message Padding

Before processing the input message, MD4 pads it to a multiple of the block size (512 bits). The padding includes the original message length in bits.

## Round Function

MD4 uses a set of three rounds of processing to update the hash value. Each round involves bitwise operations and modular addition.
```python
def F(x,y,z):
    return (x & y) | (~x & z)

def G(x,y,z):
    return (x & y) | (x & z) | (y & z)

def H(x,y,z):
    return (x ^ y ^ z)

def Circular_LShift(x,y):
    x = x & 0xffffffff
    return (((x) << (y)) | ((x) >> (32-(y)))) & 0xffffffff

def round1(a,b,c,d,k,s):
    return (Circular_LShift((a + F(b,c,d) + k),s)) & 0xffffffff

def round2(a,b,c,d,k,s):
    return (Circular_LShift((a + G(b,c,d) + k + 0x5A827999),s)) & 0xffffffff

def round3(a,b,c,d,k,s):
    return (Circular_LShift((a + H(b,c,d) + k + 0x6ED9EBA1),s)) & 0xffffffff
```
## Final Hash Value

The final hash value is the concatenation of the four 32-bit words (A, B, C, D) produced during the processing rounds.

## Example Usage

```python
import hashlib
from MD4 import MD4 as my_MD4

Message = b"This is a test for MD4 !!!"

my = my_MD4.MD4(Message)
Hashlib = hashlib.new('md4')
Hashlib.update(Message)
Hashlib = Hashlib.hexdigest()

assert my == Hashlib
print(f"Tryly {my} == {Hashlib}")

```
```bash
Tryly ce71b0eec45017ee04b7d315874bdafb == ce71b0eec45017ee04b7d315874bdafb
```
