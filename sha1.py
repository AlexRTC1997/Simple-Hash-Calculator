# SHA-1 Functions
def ROTL(x, n, w):
    return (x << n & (2 ** w - 1)) | (x >> w - n)


def Ch(x, y, z):
    return (x & y) ^ (~x & z)


def Parity(x, y, z):
    return x ^ y ^ z


def Maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

# Return the SHA-1 hash result
def sha1(x):
    K = []

    for t in range(80):
        if t <= 19:
            K.append(0x5a827999)
        elif t <= 39:
            K.append(0x6ed9eba1)
        elif t <= 59:
            K.append(0x8f1bbcdc)
        else:
            K.append(0xca62c1d6)

    x_bytes = bytearray(x, 'ascii')

    x_bits = [format(x, '08b') for x in x_bytes]

    x_bits_string = ''.join(x_bits)

    # Padding
    pad_bits = '1' + ('0' * (448 - (8 * len(x) + 1))) + format(len(x) * 8, '064b')

    x_padded = x_bits_string + pad_bits
    assert (len(x_padded) == 512)

    M1 = x_padded
    H = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0]
    N = 1

    # Rounds
    for i in range(1, N + 1):
        W = list()

        for t in range(80):

            if t <= 15:
                W.extend([int(M1[(32 * t): (32 * (t + 1))], 2)])
            else:
                W.extend([ROTL(W[t - 3] ^ W[t - 8] ^ W[t - 14] ^ W[t - 16], n=1, w=32)])

        a = H[0]
        b = H[1]
        c = H[2]
        d = H[3]
        e = H[4]

        for t in range(80):
            if t <= 19:
                f = Ch
            elif t <= 39:
                f = Parity
            elif t <= 59:
                f = Maj
            else:
                f = Parity

            T = (ROTL(a, n=5, w=32) + f(b, c, d) + e + K[t] + W[t]) % (2 ** 32)
            e = d
            d = c
            c = ROTL(b, n=30, w=32)
            b = a
            a = T

        H[0] = (a + H[0]) % (2 ** 32)
        H[1] = (b + H[1]) % (2 ** 32)
        H[2] = (c + H[2]) % (2 ** 32)
        H[3] = (d + H[3]) % (2 ** 32)
        H[4] = (e + H[4]) % (2 ** 32)

        # Format result
        H = [format(x, '08x') for x in H]

        return "".join(H)
