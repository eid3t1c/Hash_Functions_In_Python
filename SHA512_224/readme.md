# SHA-512/224 Hash Function

## Properties

- **Digest Size:** 224 bits (28 bytes)
- **Block Size:** 1024 bits (128 bytes)
- **Rounds:** 80

## Initialization

SHA-512/224 uses a set of constant initial values (also known as round constants) and an initial hash value (H0) as part of its initialization.
In SHA-512/224, the initial hash values (H0 to H7) are derived from the SHA-512 hash function's default initial state, modified by XORing it with specific constants.

- Initial Hash Value (H0 to H7):
  - H0 = 8c3d37c819544da2
  - H1 = 73e1996689dcd4d6
  - H2 = 1dfab7ae32ff9c82
  - H3 = 679dd514582f9fcf
  - H4 = 0f6d2b697bd44da8
  - H5 = 77e36f7304c48942
  - H6 = 3f9d85a86a1d36c8
  - H7 = 1112e6ad91d692a1

## Round Constants

SHA-512/224 uses a set of constant round values (K) during each round of processing. These values are derived from the fractional parts of the cube roots of the first 80 prime numbers.

- Round Constants (K0 to K79):
  - K0 = 428a2f98d728ae22
  - K1 = 7137449123ef65cd
  - K2 = b5c0fbcfec4d3b2f
  - ...
  - K77 = 597f299cfc657e2a
  - K78 = 5fcb6fab3ad6faec
  - K79 = 6c44198c4a475817


## Message Padding

Before processing the input message, SHA-512/224 pads it to a multiple of the block size (1024 bits). The padding includes the original message length in bit-bytes.

## Round Function

During each round of processing, SHA-512/224 uses a set of logical functions and bitwise operations to update the hash value.

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

The final hash value is the concatenation of the first 4 64-bit words (H0 to H3) produced during the processing rounds.
