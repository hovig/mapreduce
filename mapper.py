inputFile = open("purchases.txt",'r')
outputFile = open("mapper_output.txt", 'w')
for curr in inputFile:
    data = curr.strip().split("\t")
    if(len(data)!=6):
        continue
    try:
        if data[3] == "Toys" or data[3] == "Consumer Electronics":
            outputFile.write(data[3] + "\t" + data[4]+"\n")
    except Exception:
        print("")
