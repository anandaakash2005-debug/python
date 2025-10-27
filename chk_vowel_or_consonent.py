ch=input("Enter a single Alphabet: ")

if len(ch) == 1 and ch.isalpha():
    ch=ch.lower()
    if ch in ['a','e','i','o','u']:
        print(ch," is a vowel")
    else:
        print(ch," is a consonent")
else:
    print("Invalid input! please enter a single alphabet.")