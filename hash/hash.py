import hashlib

h = hashlib.md5(b'password')
digest_size = h.digest_size  # The size of the resulting hash in bytes
block_size = h.block_size  # The internal block size of the hash algorithm in bytes
print(h.hexdigest())
print(digest_size)
print(block_size)

text = input(f'Введите текст: ')
hash_ = hashlib.md5(text.strip().encode('utf-8'))  # utf-8 necessarily!
hash_1 = hashlib.sha1(text.strip().encode('utf-8'))  # utf-8 necessarily!
# Record
file = open('myhash.txt', 'a')
file.write(f'Ваш хэш: {hash_.hexdigest()} - {text}\n')
file.close()
print(f'Ваш хэш: {hash_.hexdigest()}')
