string = input ("Enter a String: ")

vowels=0

consonants=0

for Q in string:
    if (Q== 'A' or Q== 'E' or Q=='I' or Q=='0' or Q=='U' or Q== 'a' or Q=='e' or Q== 'i' or Q== 'o' or Q== 'u'):
        vowels = vowels+1.
    else:
        consonants = consonants+1

print ("The number of Vowels is", vowels,".")
print("The number of Consonants is", consonants, ".")
