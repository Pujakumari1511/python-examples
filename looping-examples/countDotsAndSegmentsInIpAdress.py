ipAddress = input("Enter an IP address: ")
#print(number.count("."))
countOfDot = 0
segmentOfLength = 0
for char in ipAddress:
    if char == ".":
        countOfDot = countOfDot + 1
print("no of segments = ", countOfDot+1)

# segments = number.split(".")  #This is used witn split function
# for segment in segments:
#     print(len(segment))

#Both logic gives same result
for character in ipAddress:  #This is use without splitting

    if character != ".":
        segmentOfLength = segmentOfLength + 1
        continue
    print("segment of length = ",segmentOfLength)
    segmentOfLength = 0
print("segment of length = ",segmentOfLength)