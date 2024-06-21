#utilts
import os
import json
import json5
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

def extract_and_stringify_object(original):
    for i in range(0, len(original)):
        if original[i] == '{':
            start = i
            break
    for i in range(len(original) - 1, -1, -1):
        if original[i] == '}':
            end = i
            break  
    if end < len(original) - 1 and original[end + 1] != ',':
        original = original[:end + 1] + ',' + original[end + 1:]
    return json.dumps(json5.loads(original[start:end + 1]), indent=4)

def printJsonToFile(data, filename):
    #Creating a file if not exist
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write('')
    with open (filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, indent=4))
    return True