'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
def decrypt_substitution(ciphertext,key):
    plaintext=""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                decrypted_char = key[char]
                plaintext+= decrypted_char
            else:
                decrypted_char=key[char.upper()].upper()
            
                plaintext+= decrypted_char
        else:
            plaintext+= char
        
    return plaintext
ciphertext="ABC"
key  =  {
        'A':'X',
        'B':'Y',
        'C':'Z'}    
plaintext = decrypt_substitution(ciphertext,key)
print("decrypted text",plaintext)              
    
