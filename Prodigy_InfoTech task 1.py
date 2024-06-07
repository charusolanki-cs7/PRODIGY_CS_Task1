#TASK 1
#Implement Caesar Cipher


Letters=['a','b','c','d','e','f','g','h','i','j','k','l','m',
         'n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in Letters:
            position = Letters.index(char)
            new_position=(position + shift_key)%26
            cipher_text += Letters[new_position]
        else:
            cipher_text +=char
    print("TEXT AFTER ENCRYPTION:",cipher_text)
        
def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        if char in Letters:
            position = Letters.index(char)
            new_position=(position - shift_key)%26
            plain_text += Letters[new_position]
        else:
            plain_text +=char
    print("TEXT AFTER DECRYPTION:",plain_text)
g=True
while True:
    Task_to_do=input("Write 'encrypt' for encryption , Write 'decrypt' for descryption:\n")
    text=input("Write your message here:\n").lower()
    shift=int(input("Enter shift key:\n"))
    if Task_to_do=="encrypt":
        encryption(plain_text= text,shift_key= shift)
    else:
        decryption(cipher_text= text,shift_key= shift)

    ans=input("Type 'Yes' to contine and 'No' to end the program:\n")
    if ans=='yes':
        continue
    else:
        print("Program is over")
        break
