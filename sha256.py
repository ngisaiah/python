from hashlib import sha256

print('enter passwd:')
passwd = input()
hash = sha256(passwd.encode()).hexdigest()

print('Hashed passwd:' + hash)