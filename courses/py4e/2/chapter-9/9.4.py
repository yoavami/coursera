# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail
# messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the
# mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
# they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum
# loop to find the most prolific committer.

fname = input("Enter the file name: ")
fname = fname + ".txt"

try:
    fhand = open(fname, 'r')
except:
    print("File cannot be opened", fname)
    quit()

counts = dict()

for line in fhand:
    if line.startswith("From:"):
        continue
    if line.startswith("From"):
        words = line.split()
        person = words[1]
        counts[person] = counts.get(person, 0) + 1

maxperson = None
maxvalue = None

for k, v in counts.items():
    if maxvalue is None or v > maxvalue:
        maxperson = k
        maxvalue = v

print(maxperson, maxvalue)

