

def encrypt_vigenere(plaintext, keyword):
	"""
	>>> encrypt_vigenere("PYTHON", "A")
	'PYTHON'
	>>> encrypt_vigenere("python", "a")
	'python'
	>>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
	'LXFOPVEFRNHR'
	"""
	ciphertext = ''
	for index, ch in enumerate(plaintext):
		if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
			change = ord(keyword[index % len(keyword)])
			change -= ord('a') if ('a' <= ch <= 'z') else ord('A')
			code = ord(ch) + change
			if ('a' <= ch <= 'z') and code > ord('z'):
				code -= 26
			elif ('A' <= ch <= 'Z') and code > ord('Z'):
				code -= 26
			ciphertext += chr(code)
		else:
			chiphertext += ch
	return ciphertext


def decrypt_vigenere(mag, keyword):
	"""
	>>> decrypt_vigenere("PYTHON", "A")
	'PYTHON'
	>>> decrypt_vigenere("python", "a")
	'python'
	>>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
	'ATTACKATDAWN'
	"""
	plaintext = ''
	for index, ch in enumerate(mag):
		if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
			change = ord(keyword[index % len(keyword)])
			change -= ord('a') if ('a' <= ch <= 'z') else ord('A')
			code = ord(ch) - change
			if ('a' <= ch <= 'z') and code < ord('a'):
				code += 26
			elif ('A' <= ch <= 'Z') and code < ord('A'):
				code += 26
			plaintext += chr(code)
		else:
			plaintext += ch
		return plaintext
