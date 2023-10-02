# SHA-512/256 Hash Function

## Properties

- **Digest Size:** 256 bits (32 bytes)
- **Block Size:** 1024 bits (128 bytes)
- **Rounds:** 80

## Initialization

SHA-512/256 uses a set of constant initial values (also known as round constants) and an initial hash value (H0) as part of its initialization.

- Initial Hash Value (H0 to H7):
  - H0 = 22312194FC2BF72C
  - H1 = 9F555FA3C84C64C2
  - H2 = 2393B86B6F53B151
  - H3 = 963877195940EABD
  - H4 = 96283EE2A88EFFE3
  - H5 = BE5E1E2553863992
  - H6 = 2B0199FC2C85B8AA
  - H7 = 0EB72DDC81C52CA2

## Round Constants

SHA-512/256 uses a set of constant round values (K) during each round of processing. These values are derived from the fractional parts of the cube roots of the first 80 prime numbers.

- Round Constants (K0 to K79):
  - K0 = 428a2f98d728ae22
  - K1 = 7137449123ef65cd
  - K2 = b5c0fbcfec4d3b2f
  - ...
  - K77 = 597f299cfc657e2a
  - K78 = 5fcb6fab3ad6faec
  - K79 = 6c44198c4a475817


## Message Padding

Before processing the input message, SHA-512/256 pads it to a multiple of the block size (1024 bits). The padding includes the original message length in bit-bytes.

## Round Function

During each round of processing, SHA-512/256 uses a set of logical functions and bitwise operations to update the hash value.

```python
def Right_Shift(x, y):
    return x >> y

def Rotate_Right(x, y):
    return (x >> y) | (x << (64 - y)) & 0xFFFFFFFFFFFFFFFF

def Sigma0(x):
    return Rotate_Right(x, 28) ^ Rotate_Right(x, 34) ^ Rotate_Right(x, 39)

def Sigma1(x):
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

The final hash value is the concatenation of the first 4 64-bit words (H0 to H3) produced during the processing rounds.
