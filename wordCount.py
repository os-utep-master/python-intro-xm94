import sys
import re
import string

def main():
    o = "output"
    wordCounts={}#dictionary containing the counts
    with open("declaration.txt",'r') as inputFile:
        for line in inputFile:
            line = line.strip()
            noPunct = string.maketrans(string.punctuation, ' '*len(string.punctuation))
            line = line.translate(noPunct)#removes punctuatuion
            line = line.lower()#changing to all lowercase
            words = re.split('[ \t]', line)#splitting into individual words
            for word in words:
                if word in wordCounts:#adds to the count
                    wordCounts[word]+=1
                else:#adds to the dictionary and sets it to 1
                    if word != "":#putting in because the blank character kept showing up
                        wordCounts[word]=1
        inputFile.close()
    sortedKeys = sorted(wordCounts.iterkeys())#sorts the keys
    f = open(o + ".txt",'w+');
    for keys in sortedKeys:
        f.write(keys + " " + str(wordCounts[keys]) + "\n")

    f.close();

if __name__ =='__main__':
    main()
