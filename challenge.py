import csv
with open('treeorderssubsetnodupes.csv', mode='r') as infile:
    reader = csv.reader(infile)

    mydict = {}

    for row in reader:
        key = row[0]
        mydict[key] = row[1]

    print(len(mydict))
    mydict['205']=10
    print(mydict)

    mydict['999'] = 12

    print(mydict)