#utilts
import os
import json
def printSoupToHtml(soup):
    #Creating a file if not exist
    if not os.path.exists('soup.html'):
        with open('soup.html', 'w', encoding='utf-8') as file:
            file.write('')
    with open('soup.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))
    return True
def printSoupToJson(soup):
    #Creating a file if not exist
    if not os.path.exists('soup.json'):
        with open('soup.json', 'w', encoding='utf-8') as file:
            file.write('')
    with open('soup.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(soup))
    return True

def getStringBetweenTwoWords(string, first, last):
    try:
        start = string.index(first) + len(first)
        end = string.index(last, start)
        return string[start:end]
    except ValueError:
        return ""

