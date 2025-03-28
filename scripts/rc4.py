# see wikipedia https://en.wikipedia.org/wiki/RC4
def encrypt_rc4(dat: bytes, key: bytes):
    S = []
    for i in range(256):
        S.append(i)
    j = 0
    keylength = len(key)
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]
    i = 0
    j = 0
    out = []
    for ch in dat:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = ch ^ S[(S[i] + S[j]) % 256]
        out.append(k)
    return bytes(out)
