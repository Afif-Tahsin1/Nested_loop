string = input("Please enter your own word here: ")
char = input("Please enter your own character: ")
i = 0
count = 0
while (i<len(string)):
    if string[i] == char:
        count = count + 1

        i = i+1
print(f"The total number of char  {char} has been Occured {count} times")