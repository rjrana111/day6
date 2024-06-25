pal = input("ENTER ANY WORD: ")
cleaned_pal = pal.replace(" ", "").upper()

if cleaned_pal == cleaned_pal[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")




