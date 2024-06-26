Agent James prepares to transmit vital information to his superiors. In the quest for heightened security, Agent James entrusted Python developers to fortify his message encryption. After exploring various ciphers, they decided to combine Route Cipher, Rail Fence Cipher, Substitution Cipher with custom cipher kk cipher. Now, armed with this amalgamation of ciphers, James can transmit vital information with confidence.

a) Route Cipher Encryption

Creating a Control Message To understand how to do this, create your own message and route cipher. Call this your control message:

• Number of columns = 4

• Number of rows = 5

• Start position = Bottom left

• Route = Alternating up and down columns

• Plaintext = 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

• Ciphertext = 16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19

• Key = –1 2 –3 4

Using a numeric progression for the plaintext allows you to instantly tell whether you’ve gotten all or part of the decryption correct, at any place within the message

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/1aa65418-6f5c-411d-8e3e-9bb8637df177)

The key keeps track of both the order and direction of the route through the columns. The route doesn’t have to move through the columns in order. For instance, it can move down the first column, up the third, down the fourth, and finally up the second. Negative numbers mean you start at the bottom and read up a column; positive numbers mean the reverse. For the control message, the final key used in the program will be a list: [–1, 2, –3, 4]. This list will instruct the program to start reading up from the bottom of column 1, move to the top of column 2 and read down, move to the bottom of column 3 and read up, and move to the top of column 4 and read down. Note that you shouldn’t use 0 in keys because the users, being human, prefer to start counting at 1. Of course, Python prefers to start counting at 0, so you’ll need to subtract 1 from the key values behind the scenes. Everybody wins!

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/5b5df632-b66e-4e18-acc0-b9dd7d25461f)

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/41aff8b6-4717-44a7-b736-0036f0824f11)

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/390281d0-1486-4608-9d0e-3b78d87cba7e)



b) Rail Fence Cipher Encryption

Confederate officers and spies were pretty much on their own when it came to cryptography. This led to unsophisticated solutions, one of the favorites being the rail fence cipher, so named due to its resemblance to the zigzag pattern of a split-rail fence.

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/75508ebb-3791-4744-917d-7da082ed4daa)

The rail fence is a simple-to-use transposition cipher, like the Union’s route cipher, but differs from the route cipher in that it transposes letters rather than words, making it more error-prone. And since the number of possible keys is much more restrictive than the number of paths through a route cipher, the rail fence cipher is much easier to “tear down.”

The Strategy

To Encrypt a message with rail fence cipher, follow the following steps
![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/c60802d9-c993-4202-93ba-0203a7a45923)

After the plaintext is written, the spaces are removed, and all the letters are converted to uppercase (Step 2). Using uppercase is common convention in cryptography, as it obfuscates the presence of proper names and the beginning of sentences, giving a crypt analyst fewer clues for deciphering the message. The message is then written in stacked fashion, with every other letter below the previous letter and shifted over one space (Step 3). This is where the “rail fence” analogy becomes apparent. The first row is then written, followed immediately by the second row on the same line (Step 4), and then the letters are broken into groups of five to create the illusion of distinct words and to further confuse the crypt analyst (Step 5).

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/0928a530-3bf0-4820-a35b-bc4fe30a7d2c)

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/496b14ce-0318-4115-90d3-5a237d094833)



c) Substitution Cipher Encryption

Substitution cipher encryption involves replacing each plaintext letter with a different letter in a random way.

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/816f0ce4-e4ad-4883-9c96-46e8b8f03e29)

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/1462452b-15d7-4e5d-98c9-63402e567ee1)

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/d6080ca0-4a0d-46f2-8698-5942ab741dfe)



d) My Cipher Encryption

Replacing alphabets with particular values.
![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/b11deb0a-a894-4d58-9f89-8a6cafc5690b)

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/b3148c92-e852-48b8-b360-c1be2e1b92fe)

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/6eefaac5-8514-46ad-8fef-a79c6707885b)




Deciphering Danger: Race Against Time

Agent Sarah, receiving a crucial encrypted message from her trusted ally, Agent James, understands the urgency. With time ticking away, she diligently decrypts the message, knowing the gravity of the situation. Employing her expertise, Sarah tackles the complex ciphers — kk cipher, Substitution cipher, Rail Fence cipher, and Route cipher with precision and determination. Finally, with the decrypted message in hand, Sarah unveils the hidden truth within.

a) kk Cipher Decryption

Replacing alphabets to original alphabets based on kk cipher encryption

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/0bd78104-2681-4b75-af24-ed26063beb2e)

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/526e0089-7a4f-4541-ad7b-c66bd3289317)



b) Substitution Cipher Decryption

Replacing alphabets with random interchange of alphabets.

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/27720ae9-505d-40c2-8054-c606864f1f41)

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/24c696e4-9a74-476d-a0ba-423b99227dfc)

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/f5784f2e-d98b-4130-b85a-494c7ef62e97)



c) Rail Fence Cipher Decryption

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/bc53f71c-26b2-4323-b329-8af86000d821)

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/1a32d34f-e944-4ef3-bf01-40dc94f2667e)

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/dd2718ce-8ed4-40b6-9ca0-7dd9b74e0e2b)

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/fa642989-46ad-4a7b-851d-72a26ca2e792)

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/cb136df4-8361-49ff-9672-3743473a188d)



d) Route Cipher Decryption

Designing, Populating, and Depopulating the Matrix

You’ll input the ciphertext as a continuous string. For your program to unravel the route through this string, you’ll first need to build and populate a translation matrix. The ciphertext string is just the columns in the transposition matrix laid end to end, in the order they were read. And as there are five rows in the transposition matrix, every group of five elements in the ciphertext represents a separate column. You can represent this matrix with a list of lists:

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/34de3beb-0aeb-4e99-ad57-80a044b1c824)

The items in this new list now represent lists — with each list represent[1]ing a column — and the five elements in each list represent the rows that comprise that column. This is a little hard to see, so let’s print each of these nested lists on a separate line:

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/58a490d2-b997-41f5-8c34-9b316c00db71)

If you read each list left to right, starting at the top, you follow the trans[1]position route, which was up and down alternate columns. From Python’s point of view, the first column read is list-of-lists[0], and the starting point is list-of-lists[0][0]. Now, normalize the route by reading all columns in the same direction as the starting column (up). This requires reversing the order of elements in every other list, as shown in bold here:

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/4edcf500-3f7b-4beb-ae51-9407ecd8bd53)

A pattern emerges. If you start at the upper right and read down each column, ending at the lower left, the numbers are in numerical order; you’ve restored the plaintext! To replicate this, your script can loop through every nested list, removing the last item in that list and adding the item to a new string, until the Decoding American Civil War Ciphers 69 translation matrix has been emptied. The script will know from the key which nested lists it needs to reverse and the order in which to depopulate the matrix. The output will be a string of the restored plaintext:

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/2f80547b-1362-40f1-8a19-2915a441cc4f)

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/5f52d8ce-fc28-4ea6-9bb8-c16ecab96f5a)

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/eeefc5e4-b80d-4321-9829-428f5336095d)

![image](https://github.com/koushikkatakam/cipher_and_decipher/assets/116490778/34bf24a7-5312-443c-9754-052b7e90dce0)

With a sense of purpose and determination, Sarah transmits the decrypted message to her superiors, alerting them to the imminent danger.
































