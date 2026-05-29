#in this code i will creat a code that will check how many times the vowels appear in a given text

countVowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

phrase = input("write a phrase:").lower()  #the .lower() method is used to convert the input to lowercase, so that the counting of vowels is case-insensitive

for char in phrase: 
    if char in countVowels:
        countVowels[char] += 1

print("\n\n---result---:")

for vowels, quant in countVowels.items():
    print(f"the vowel {vowels} appears {quant} time(s) in the phrase.")


