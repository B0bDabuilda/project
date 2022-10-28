import math
import time

prompt1 = "Hi!"
print(prompt1)
time.sleep(2)

prompt2 = "I check how many vowels are contained in words. How useless - right?"
print(prompt2)

time.sleep(2)

single_word = input("Please input your word: ")

count1 = 0

for b in single_word:
        if (b == "e") or (b == "a") or (b == "i") or (b == "o") or (b == "u"):
            count1 = count1 + 1

print(f"There are {count1} vowels in the word {single_word}.")
        
#Completed - had to recheck the or statements and the joinment of different conditions. Apart from that, everything is alright.