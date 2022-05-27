# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of
# the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a
# second time using a colon. From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 Once you have accumulated the
# counts for each hour, print out the counts, sorted by hour as shown below.

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
        hours = words[5].split(':')
        time = hours[0]
        counts[time] = counts.get(time, 0) + 1

lst = list()

for k, v in counts.items():
    lst.append( (k, v) )

lst.sort()

for k, v in lst:
    print(k, v)










