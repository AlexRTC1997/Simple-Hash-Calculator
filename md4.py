import struct


class MD4:
    width = 32
    mask = 0xFFFFFFFF

    # Little-endian
    h = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]

    def __init__(self, message):
        self.msg = message

        # Pre-processing: Total length is a multiple of 512 bits.
        ml = len(message) * 8
        message += b"\x80"
        message += b"\x00" * (-(len(message) + 8) % 64)
        message += struct.pack("<Q", ml)

        # Process the message in successive 512-bit chunks.
        self._process([message[i: i + 64] for i in range(0, len(message), 64)])

    # Return the final hash value as a `bytes` object
    def bytes(self):
        return struct.pack("<4L", *self.h)

    # Return the final hash value as hexbytes
    def hexbytes(self):
        return self.hexdigest().encode

    # Return the final hash value as a hex string
    def hexdigest(self):
        return "".join(f"{value:02x}" for value in self.bytes())

    def _process(self, chunks):
        for chunk in chunks:
            X, h = list(struct.unpack("<16I", chunk)), self.h.copy()

            # Round 1.
            Xi = [3, 7, 11, 19]
            for n in range(16):
                i, j, k, l = map(lambda x: x % 4, range(-n, -n + 4))
                K, S = n, Xi[n % 4]
                hn = h[i] + MD4.F(h[j], h[k], h[l]) + X[K]
                h[i] = MD4.lrot(hn & MD4.mask, S)

            # Round 2.
            Xi = [3, 5, 9, 13]
            for n in range(16):
                i, j, k, l = map(lambda x: x % 4, range(-n, -n + 4))
                K, S = n % 4 * 4 + n // 4, Xi[n % 4]
                hn = h[i] + MD4.G(h[j], h[k], h[l]) + X[K] + 0x5A827999
                h[i] = MD4.lrot(hn & MD4.mask, S)

            # Round 3.
            Xi = [3, 9, 11, 15]
            Ki = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
            for n in range(16):
                i, j, k, l = map(lambda x: x % 4, range(-n, -n + 4))
                K, S = Ki[n], Xi[n % 4]
                hn = h[i] + MD4.H(h[j], h[k], h[l]) + X[K] + 0x6ED9EBA1
                h[i] = MD4.lrot(hn & MD4.mask, S)

            self.h = [((v + n) & MD4.mask) for v, n in zip(self.h, h)]

    # Function F
    @staticmethod
    def F(x, y, z):
        return (x & y) | (~x & z)

    # Function G
    @staticmethod
    def G(x, y, z):
        return (x & y) | (x & z) | (y & z)

    # Function H
    @staticmethod
    def H(x, y, z):
        return x ^ y ^ z

    # Left rotation
    @staticmethod
    def lrot(value, n):
        lbits, rbits = (value << n) & MD4.mask, value >> (MD4.width - n)
        return lbits | rbits


# Return MD4 Hash
def md4(message):
    return MD4(message).hexdigest()


# === SIMPLE VERSION ===
"""
import hashlib


def md4(text):
    return hashlib.new("md4", text).hexdigest()
"""
