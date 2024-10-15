def getBookText(path):
    with open(path) as f:
        return f.read()

def getWordsCount(text):
    return len(text.split())

def getCharsCount(text):
    result = {}
    for t in text.lower():
        if t.isalnum():
            if t not in result:
                result[t] = 1
            else:
                result[t] += 1
    return result

def createReport(path, wordCount, charCountDict):
    print(f"--- Begin report of {path} ---")
    print(f"There are {wordCount} words in the document")
    sortedCharsDict = sorted(charCountDict.items(), key=lambda x:x[1], reverse=True)
    for char in sortedCharsDict:
        print(f"The '{char[0]}' character was found {char[1]} times")
    print("--- End report ---")



def main():
    path = "books/frankenstein.txt"
    text = getBookText(path)
    wordsCount = getWordsCount(text)
    charsCountDict = getCharsCount(text)
    createReport(path, wordsCount, charsCountDict)

main()
