import porter
import spell
import json
  
def binary_search(words, word_to_search):
    l = 0
    r = len(words)
    while (l<=r):
        middle = (l+r)//2
        if word_to_search == words[middle]:
            return True
        if word_to_search > words[middle]:
            l = middle+1
        else:
            r = middle-1
    return False

def search_word(word):
    word = porter.stem(word)
    if binary_search(list(posting_lists.keys()), word)==True:
        docs = posting_lists[word]
        return docs
    else:
        return 'The word has not been found in any of the available documents'

f = open('posting_lists.json', 'r')
posting_lists = json.load(f)
f.close()

f = open('words.txt')
words = f.read().lower().split()
f.close()

f = open('p_c.json', 'r')
p_c = json.load(f)
f.close()


#binary_search_bisect(words, word_to_search)==False
result = []
while True:
    word_to_search = input('Search for: ').lower()
    if (binary_search(words, word_to_search)==False):
        candidates = spell.correct_word(word_to_search, 2, 0.01, p_c, words)
        print('The word is mispelled, here are some possible alternatives:\n', list(set(candidates)))
        input_ = input('Do you want to change your query?  [Y/N] ')
        if input_ in ['Y','y']:
            continue
        elif input_ in ['N','n']:
            break
        else: 
            print("The answer can only be 'y' or 'n'")
            break
    else:
        result = search_word(word_to_search)
        print(result)
        break


    
    

