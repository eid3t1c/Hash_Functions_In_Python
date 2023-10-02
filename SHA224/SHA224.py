def Default_State(): # Default State
    return [0xc1059ed8, 0x367cd507, 0x3070dd17, 0xf70e5939, 0xffc00b31, 0x68581511, 0x64f98fa7,0xbefa4fa4]

def pad(message,l): # SHA-224  padding implementation
    final = []
    p = message + b"\x80" + b"\x00" * ((64 - l - 1 - 8) % 64) + (l*8).to_bytes(8,byteorder="big")
    blocks = [p[x:x+64] for x in range(0,len(p),64)]
    for b in blocks:
        final.append([int.from_bytes(b[x:x+4],"big") for x in range(0,len(b),4)])
    
    return  final

# SHA-224 Functions
def Shift_Right(x,y):
    return x >> y

def Rotate_Right(x,y):
    return (x >> y) | (x << (32 - y)) & 0xffffffff

def sigma0(x):
    return Rotate_Right(x,7) ^ Rotate_Right(x,18) ^ Shift_Right(x,3)

def sigma1(x):
    return Rotate_Right(x,17) ^ Rotate_Right(x,19) ^ Shift_Right(x,10)

def Ch(x,y,z):
    return (x & y) ^ (~x & z)

def Maj(x,y,z):
    return (x & y) ^ (x & z) ^ (y & z)

def Sigma0(x):
    return Rotate_Right(x,2) ^ Rotate_Right(x,13) ^ Rotate_Right(x,22)

def Sigma1(x):
    return Rotate_Right(x,6) ^ Rotate_Right(x,11) ^ Rotate_Right(x,25)

# SHA-224 constant 64  32 bit words
K = bytearray.fromhex("428a2f9871374491b5c0fbcfe9b5dba53956c25b59f111f1923f82a4ab1c5ed5"
                      "d807aa9812835b01243185be550c7dc372be5d7480deb1fe9bdc06a7c19bf174"
                      "e49b69c1efbe47860fc19dc6240ca1cc2de92c6f4a7484aa5cb0a9dc76f988da"
                      "983e5152a831c66db00327c8bf597fc7c6e00bf3d5a7914706ca635114292967"
                      "27b70a852e1b21384d2c6dfc53380d13650a7354766a0abb81c2c92e92722c85"
                      "a2bfe8a1a81a664bc24b8b70c76c51a3d192e819d6990624f40e3585106aa070"
                      "19a4c1161e376c082748774c34b0bcb5391c0cb34ed8aa4a5b9cca4f682e6ff3"
                      "748f82ee78a5636f84c878148cc7020890befffaa4506cebbef9a3f7c67178f2")


K_blocks = [int.from_bytes(K[x:x+4],"big") for x in range(0,len(K),4)]


def sha224(message):

    H = Default_State()

    # Pad the message to 64 blocks
    padded_message = pad(message,len(message)) # W[:16]

    N = len(padded_message) # How many blocks

    for i in range(0,N):
        
        rounds = [padded_message[i][v] for v in range(0,16)]
        
        # Prepare the rounds
        for w in range(16,64): # W[16:64]
            rounds.append((sigma1(rounds[w-2]) + rounds[w-7] + sigma0(rounds[w-15]) + rounds[w-16]) & 0xffffffff)
        
        # Current state initialization
        a,b,c,d,e,f,g,h = H[0], H[1], H[2], H[3], H[4], H[5], H[6], H[7]

        # Shuffling
        for t in range(64):
            T1 = (h + Sigma1(e) + Ch(e,f,g) + K_blocks[t] + rounds[t]) & 0xffffffff
            T2 = (Sigma0(a) + Maj(a,b,c)) & 0xffffffff
            h = g 
            g = f
            f = e
            e = (d + T1) & 0xffffffff
            d = c 
            c = b
            b = a
            a = (T1 + T2) & 0xffffffff

        # Final state of I-th block
        H[0] += a 
        H[1] += b 
        H[2] += c 
        H[3] += d 
        H[4] += e 
        H[5] += f 
        H[6] += g 
        H[7] += h 
        H = [h & 0xffffffff for h in H]

    # Return H0||H1||H2||H3||H4||H5||H6
    return b"".join([H[f].to_bytes(4,"big") for f in range(0,len(H)-1)]).hex()

