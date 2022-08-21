p = 123456791
q = 987654323



n_rsa = p * q

print("n = ", n_rsa)

public_key = 127
private_key = 24962586124546503
data = 30120

encryption = pow(data, public_key, n_rsa)
print("rsa encryption message: ", encryption)

decryption = pow(encryption, private_key, n_rsa)
print("rsa decryption: ", decryption)