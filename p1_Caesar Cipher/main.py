from string import ascii_lowercase, ascii_uppercase

inp_string = input("Enter a string to be encrypted : ")

# enter key
en_key = input("Enter value of key : ")

# made dictionary for decryption
alp = {v: (k + int(en_key)) for k, v in enumerate(ascii_lowercase)}
alp[' '] = 999 + int(en_key)

# made dictionary for encryption
en_alp = {v: k for k, v in enumerate(ascii_lowercase)}
en_alp[' '] = 999 + int(en_key)

string = []

def get_key_dec(val):
    for key, value in alp.items():
        if val == value:
            return key


def get_key_enc(val):
    for key, value in en_alp.items():
        if val == value:
            return key


for i in range(len(inp_string)):
    string.append(alp.get(inp_string[i]))

out_string_enc = ''
for i in range(len(string)):
    out_string_enc += str(get_key_enc(string[i]))

out_string_dec = ''
for i in range(len(string)):
    out_string_dec += str(get_key_dec(string[i]))

while True:

    ch = input("Enter your choice \n 1. Encrypt \n 2. Decrypt \n 3. Exit \n")

    if int(ch) == 1:
        print("Encrypted String ", out_string_enc)
    if int(ch) == 2:
        print("Decrypted String ", out_string_dec)
        
