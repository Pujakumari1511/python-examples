letters = "abcdefghijklmnopqrstuvwxyz"

print(letters)
print(letters[25])
print(letters[-1])


backwards =(letters[25:0:-1])
print (backwards)

backwards =(letters[25::-1])
print(backwards)

threechar =(letters[16:13:-1])
print(threechar)

char3 = (letters[-10:-13:-1])
print (char3)

fivechar = (letters[-22::-1])
print(fivechar)

char5 = (letters[4::-1])
print(char5)

eightchar = (letters[25:17:-1])
print(eightchar)
char8 = (letters[:-9:-1])
print (char8)

print (letters[::5])