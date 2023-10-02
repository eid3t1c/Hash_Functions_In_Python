# MD5 (Message Digest 5) Hash Function

## Overview

- **Digest Size:** 128 bits (16 bytes)
- **Block Size:** 512 bits (64 bytes)

## Initialization

MD5 uses a set of constant initial values (also known as round constants) and an initial hash value (A, B, C, D) as part of its initialization.

- Initial Hash Value (A, B, C, D):
  - A = 0x67452301
  - B = 0xEFCDAB89
  - C = 0x98BADCFE
  - D = 0x10325476

## Constants

MD5 uses a set of constant values (K) in its rounds. Here are the correct constants for MD5:

- Constants (K):
  - K = [
    0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
    0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
    0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
    0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
    0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
    0xd62f105d, 0x2441453, 0xd8a1e681, 0xe7d3fbc8,
    0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
    0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
    0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
    0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
    0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x4881d05,
    0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
    0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
    0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
    0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
    0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391
  ]

## Message Padding

Before processing the input message, MD5 pads it to a multiple of the block size (512 bits). The padding includes the original message length in bits.

## Round Function

MD5 uses a set of four rounds of processing to update the hash value. Each round involves bitwise operations, modular addition, and logical functions.
```python
def F(x,y,z):
    return (x & y) | (~x & z)

def G(x,y,z):
    return (x & z) | (y & (~z))

def H(x,y,z):
    return (x ^ y ^ z)

def I(x,y,z):
    return (y ^ (x | (~z)))

def Circular_LShift(x,y):
    x = x & 0xffffffff
    return (((x) << (y)) | ((x) >> (32-(y)))) & 0xffffffff

def round1(a,b,c,d,k,s,i):
    return (b + Circular_LShift((a + F(b,c,d) + k + i),s)) & 0xffffffff

def round2(a,b,c,d,k,s,i):
    return (b + Circular_LShift((a + G(b,c,d) + k + i),s)) & 0xffffffff

def round3(a,b,c,d,k,s,i):
    return (b + Circular_LShift((a + H(b,c,d) + k + i),s)) & 0xffffffff

def round4(a,b,c,d,k,s,i):
    return (b + Circular_LShift((a + I(b,c,d) + k + i),s)) & 0xffffffff
```
## Final Hash Value

The final hash value is the concatenation of the four 32-bit words (A, B, C, D) produced during the processing rounds.

## Example Usage

```python
from hashlib import md5
from MD5 import MD5 as my_MD5

Message = b"This is a test for MD5 !!!"

my = my_MD5.MD5(Message)
Hashlib = md5(Message).hexdigest()

assert my == Hashlib
print(f"Tryly {my} == {Hashlib}")
```
```bash
Tryly 148d6ffd8729004f64f3fa857bae7221 == 148d6ffd8729004f64f3fa857bae7221
```
