from encryption import Encryption
from decryption import Decryption
import numpy as np
import regex as re
if __name__ == "__main__":
    # Create an object for the Encryption class
    encryption_obj = Encryption()

    # plaintext = 'innomatics Is Good For Data Sciences Innomatics Best Place To Work Innomatics Good For Jntuh Innomatics Is Best Branch For Full Stack Web Development Dev'
    # key = '-1 2 -3 4 -5'
    plaintext = input("Enter Any String Of Words In Square Matrix:")
    # print(len(plaintext.split()))
    p = 0
    for i in range(len(plaintext.split())-1,1,-1):
        if(len(plaintext.split())%i==0):
            p=i
            break

    key = ''
    for i in range(1,p+1):
        if(i%2!=0):
            key+=(str(-i)+' ')
        else:
            key+=(str(i)+' ')
    # print('key is',key)

    # print(len(plaintext.split()))

    capitalized_sentence = encryption_obj.capitalize_first_letter(plaintext)
    # print('capitalized_sentence:',capitalized_sentence)


    # Encryption
    Route_Cipher_Encryption = encryption_obj.route_cipher_encrypt(capitalized_sentence, key,p,p)
    # print("\n\nRoute cipher Encryption:  {}".format(Route_Cipher_Encryption))

    Rail_Fence_Cipher_Encryption = encryption_obj.rail_fence_cipher_encrypt(Route_Cipher_Encryption,p)
    # print("\n\nRail fence cipher Encryption: {}".format(Rail_Fence_Cipher_Encryption))

    Substitution_Cipher_Encryption = encryption_obj.substitution_cipher_encrypt(Rail_Fence_Cipher_Encryption)
    # print("\n\nSubstitution cipher Encryption:  {}".format(Substitution_Cipher_Encryption))

    kk = {
        'a': (1, 1), 'b': (1, 2), 'c': (1, 3), 'd': (1, 4), 'e': (1, 5),
        'f': (2, 1), 'g': (2, 2), 'h': (2, 3), 'i': (2, 4), 'j': (2, 5),
        'k': (3, 1), 'l': (3, 2), 'm': (3, 3), 'n': (3, 4), 'o': (3, 5),
        'p': (4, 1), 'q': (4, 2), 'r': (4, 3), 's': (4, 4), 't': (4, 5),
        'u': (5, 1), 'v': (5, 2), 'w': (5, 3), 'x': (5, 4), 'y': (5, 5),
        'z': (6, 1),'A': (6, 2), 'B': (6, 3), 'C': (6, 4), 'D': (6, 5), 'E': (6, 6),
        'F': (6,7), 'G': (6, 8), 'H': (6, 9), 'I': (7,1), 'J': (7, 2),
        'K': (7,3), 'L': (7, 4), 'M': (7, 5), 'N': (7, 6), 'O': (7, 7),
        'P': (7,8), 'Q': (7, 9), 'R': (8, 1), 'S': (8, 2), 'T': (8, 3),
        'U': (8, 4), 'V': (8, 5), 'W': (8, 6), 'X': (8, 7), 'Y': (8, 8),
        'Z': (8, 9)  
    }
    My_Cipher_Encryption = encryption_obj.kk_cipher_encrypt(Substitution_Cipher_Encryption,kk)
    # print("\n\nMy cipher Encryption:  {}".format(My_Cipher_Encryption))
    print("\n\n Message After Encryption:  {}".format(My_Cipher_Encryption))

    
    decrypted_obj = Decryption()
    My_Cipher_Decryption = encryption_obj.kk_cipher_decrypt(My_Cipher_Encryption,kk)
    # print("My Cipher Decryption:",My_Cipher_Decryption)


    Substitution_Cipher_Decryption = encryption_obj.substitutionDecrypt(My_Cipher_Decryption)
    # print("\n\nSubstitution cipher decryption:", Substitution_Cipher_Decryption)


    message = decrypted_obj.prep_ciphertext(Substitution_Cipher_Decryption)
    row1, row2 = decrypted_obj.split_rails(message)
    # print('row1=====',row1)
    # print('row2=====',row2)
    r_f_d = decrypted_obj.railFenceDecrypt(row1, row2)
    # print('\n\nRail fence cipher decryption:', r_f_d)
            
            
    words = re.findall('[A-Z][^A-Z]*', r_f_d)
    word_list = list(words)
    #         print('word list',word_list)
    split_list = [word_list[i:i+p] for i in range(0, len(word_list), p)]
    split_array = np.array(split_list)


    Rail_Cipher_Decryption = decrypted_obj.routeCipherDecrypt(split_array,p)
    # print("\n\nRoute Cipher Decryption:",Rail_Cipher_Decryption)
    print("\n\nMessage After Decrption:",Rail_Cipher_Decryption)
