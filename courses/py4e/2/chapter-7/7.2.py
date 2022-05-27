# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of
# the form: X-DSPAM-Confidence:    0.8475 Count these lines and extract the floating point values from each of the
# lines and compute the average of those values and produce an output as shown below. Do not use the sum() function
# or a variable named sum in your solution. You can download the sample data at
# http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name

fname = input("Enter the file name: ")
fname = fname + ".txt"

try:
    fhand = open(fname, 'r')
except:
    print("File cannot be opened", fname)
    quit()

counter = 0
adder = 0

for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    counter = counter + 1
    nline = line.rstrip()
    adder = adder + float(nline[(line.find("0")):])

print("Average spam confidence:", adder/counter)

