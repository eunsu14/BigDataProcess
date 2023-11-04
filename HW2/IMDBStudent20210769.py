import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

genre = dict()
with open(inputFile, "rt") as f:
    for lines in f:
        value = lines[lines.rfind(":") + 1:]
        gList = value.split('|')
        gList[-1] = gList[-1].strip('\n')

        for data in gList:
            if data not in genre:
                genre[data] = 1
            else:
                genre[data] += 1

result = ""
for key, value in genre.items():
    result += key + " " + str(value) + "\n"

with open(outputFile, "wt") as f:
    f.write(result)