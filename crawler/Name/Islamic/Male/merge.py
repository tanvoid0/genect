from string import ascii_lowercase

fout = open("male.csv", "a")
for i in ascii_lowercase:
    for line in open(i+".csv"):
        fout.write(line)
fout.close()
