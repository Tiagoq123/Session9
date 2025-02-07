fp=open("text.txt","r")
print(fp.read())
fp.close() #close is a good practice, not needed in this case
with open("text.txt","r")as fp:#this creates the context the : means that the next column should be indented to have it continue
   print(fp.read())

print("We are done, the contexts is closed by the indent")

# read from the same file, line by line
with open("text.txt","r")as fp:
    line_number = 1
    for line in fp:
        # print (line, end="")
        print(f"{line_number}: {line.rstrip()}")
        line_number+=1
