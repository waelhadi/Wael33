import zlib

def xor_decrypt(data, key):
    """فك تشفير باستخدام XOR"""
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

def decompress_data(data):
    """فك ضغط البيانات"""
    return zlib.decompress(bytes.fromhex(data)).decode('utf-8')

def main():
    encrypted_data = "..."  # البيانات المشفرة
    key = "your_key"        # المفتاح المستخدم لفك التشفير
    decrypted = xor_decrypt(decompress_data(encrypted_data), key)
    print("النص المفكوك:", decrypted)

if __name__ == "__main__":
    main()
