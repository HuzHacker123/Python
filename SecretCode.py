import random
import string
def encode(massege):
    if len(massege)>2:
        first_random= ''.join(random.choices(string.ascii_letters, k=3))
        last_random= ''.join(random.choices(string.ascii_letters, k=3))
        first_char=massege[1:]
        last_char=massege[0]
        encode_massege=first_random+first_char+last_char+last_random
        return encode_massege
    else:
        return massege[::-1]
def decode(massege):
    if len(massege)>2:
        first_char=massege[-4]
        last_char=massege[3:-4]
        decode_massege=first_char+last_char
        return decode_massege
    else:
        return massege[::-1]

for i in range(0,101):
    massege=input("Enter the secret code: ")
    action=int(input(f"Select the action you want to perform\n1.Encode\n2.Decode\n3.Exit\n(1-3): "))
    if action==1:
        print(encode(massege))
    elif action==2:
        print(decode(massege))
    else:
        print("Quiting the program.")
        break

