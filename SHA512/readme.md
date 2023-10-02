# SHA-512 Hash Function

## Properties

- **Digest Size:** 512 bits (64 bytes)
- **Block Size:** 1024 bits (128 bytes)
- **Rounds:** 80

## Initialization

SHA-512 uses a set of constant initial values (also known as round constants) and an initial hash value (H0) as part of its initialization.

- Initial Hash Value (H0 to H7):
  - H0 = 6a09e667f3bcc908
  - H1 = bb67ae8584caa73b
  - H2 = 3c6ef372fe94f82b
  - H3 = a54ff53a5f1d36f1
  - H4 = 510e527fade682d1
  - H5 = 9b05688c2b3e6c1f
  - H6 = 1f83d9abfb41bd6b
  - H7 = 5be0cd19137e2179

## Round Constants

SHA-512 uses a set of constant round values (K) during each round of processing. These values are derived from the fractional parts of the cube roots of the first 80 prime numbers.
In SHA-512/256, the initial hash values (H0 to H7) are derived from the SHA-512 hash function's default initial state, modified by XORing it with specific constants.

- Round Constants (K0 to K79):
  - K0 = 428a2f98d728ae22
  - K1 = 7137449123ef65cd
  - K2 = b5c0fbcfec4d3b2f
  - ...
  - K77 = 597f299cfc657e2a
  - K78 = 5fcb6fab3ad6faec
  - K79 = 6c44198c4a475817

## Message Padding

Before processing the input message, SHA-512 pads it to a multiple of the block size (1024 bits). The padding includes the original message length in bit-bytes.

## Round Function

During each round of processing, SHA-512 uses a set of logical functions and bitwise operations to update the hash value.
```python
def Shift_Right(x,y):
    return x >> y 

def Rotate_Right(x,y):
    return (x >> y) | (x << (64 - y)) & 0xFFFFFFFFFFFFFFFF

def sigma0(x):
    return Rotate_Right(x,1) ^ Rotate_Right(x,8) ^ Shift_Right(x,7)

def sigma1(x):
    return Rotate_Right(x,19) ^ Rotate_Right(x,61) ^ Shift_Right(x,6)

def Ch(x,y,z):
    return (x & y) ^ (~x & z)

def Maj(x,y,z):
    return (x & y) ^ (x & z) ^ (y & z)

def Sigma0(x):
    return Rotate_Right(x,28) ^ Rotate_Right(x,34) ^ Rotate_Right(x,39)

def Sigma1(x):
    return Rotate_Right(x,14) ^ Rotate_Right(x,18) ^ Rotate_Right(x,41)
```
## Final Hash Value

The final hash value is the concatenation of the 5 32-bit words (H0 to H4) produced during the processing rounds.

## Example Usage

```python
from hashlib import sha512
from SHA512 import SHA512 as my_sha512


Message = b"This is a test for SHA-512 !!!"


my = my_sha512.sha512(Message)
hashlib = sha512(Message).hexdigest()

assert my == hashlib
print(f"Tryly {my} == {hashlib}")
```
```bash
Tryly 112548f8e6da31b69e71903c43e3b015a25a88713da0ef2b126ef39e2bd29035be8bcaeec062e59516023d6c3231b63e99fd9584521638033bab0a8f59a32757 == 112548f8e6da31b69e71903c43e3b015a25a88713da0ef2b126ef39e2bd29035be8bcaeec062e59516023d6c3231b63e99fd9584521638033bab0a8f59a32757
```
