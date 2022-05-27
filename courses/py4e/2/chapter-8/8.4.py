# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the
# split() method. The program should build a list of words. For each word on each line check to see if the word is
# already in the list and if not append it to the list. When the program completes, sort and print the resulting
# words in alphabetical order. You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter the file name: ")
fname = fname + ".txt"

try:
    fhand = open(fname, 'r')
except:
    print("File cannot be opened", fname)
    quit()

lst = list()

for line in fhand:

    x = line.split()

    for i in range(len(x)):
        if x[i] not in lst:
            lst.append(x[i])

lst.sort()
print(lst)