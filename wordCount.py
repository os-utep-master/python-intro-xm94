import sys
import re
import string

def main():
    if len(sys.argv) is not 3:
        print("Correct usage: wordCount.py <input text file> <output text file>")
        exit()

    inputText = sys.argv[1]
    outputText = sys.argv[2]#a string ending in .txt that will be output to
    wordCounts={}#dictionary containing the counts
    with open(inputText,'r') as inputFile:
        for line in inputFile:
            line = line.strip()#removes newlines
            noPunct = str.maketrans(string.punctuation, ' '*len(string.punctuation))#translates punctuation to spaces
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
    sortedKeys = sorted(iter(wordCounts.keys()))#sorts the keys
    f = open(outputText,'w+');#output file named output.txt
    for keys in sortedKeys:#loops through the dictionary in alphabetical order
        f.write(keys + " " + str(wordCounts[keys]) + "\n")
    f.close();

if __name__ =='__main__':
    main()
