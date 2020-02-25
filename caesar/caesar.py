
def encrypt_caesar(plaintext):
	"""
	>>> encrypt_caesar("PYTHON")
	'SBWKRQ'
	>>> encrypt_caesar("python")
	'sbwkrq'
	>>> encrypt_caesar("Python3.6")
	'Sbwkrq3.6'
	>>> encrypt_caesar("")
	''
	"""
	ciphertext = ""
	for i in plaintext:
		if "a" <= i <= "z" or "A" <= i <= "Z":
			c = ord(i) + 3
			if ord("Z") < c < ord("a") or c > ord("z"):
				c -= 26
			ciphertext += chr(c)
		else:
			ciphertext += i
	return ciphertext


def decrypt_caesar(ciphertext):
	"""
	>>> decrypt_caesar("SBWKRQ")
	'PYTHON'
	>>> decrypt_caesar("sbwkrq")
	'python'
	>>> decrypt_caesar("Sbwkrq3.6")
	'Python3.6'
	>>> decrypt_caesar("")
	''
	"""
	plaintext = ""
	for i in ciphertext:
		if "a" <= i <= "z" or "A" <= i <= "Z":
			c = ord(i) - 3
			if ord("Z") < c < ord("a") or c < ord("A"):
				c += 26
			plaintext += chr(c)
		else:
			plaintext += i
	return plaintext
