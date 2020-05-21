from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

iv = b'\xd9H\xaf\xc9\xa5\xc9"3\x93\xaa\xbd\x87\xa5\x15\x04\xdd'
key = b'0123456789abcdef0123456789abcdef'

cipher = AES.new(key,AES.MODE_CBC,iv)

msg = b'03LPYOV{How_many_nice_things_can_you_find_1_bit_at_the_time?}'
# msg = b'03LPYOV{How_many_nice_things_can_you_find_1_bit_at_the_time????}'

print(len(msg))
print(iv)
print(key)
ctxt = cipher.encrypt(pad(msg,AES.block_size))
print(ctxt)

cipher2 = AES.new(key,AES.MODE_CBC,iv)
print(cipher2.decrypt(ctxt))
