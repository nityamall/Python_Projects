str1=input("Enter a word --> ")
str1=str1.casefold();
str2=reversed(str1)
if list(str1)==list(str2):
    print("Palindrome")
else:
    print("Not Palindrome")