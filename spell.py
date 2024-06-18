import math as m

def readwords(list):
    counters = {}
    total = 0
    for word in list:
        total += 1
        if word in counters:
            counters[word] += 1
        else:
            counters[word] = 1
    probs = {}
    for word in counters:    # P(C)
        probs[word] = counters[word]/total
    
    return probs



def error_prob (e, n, q):
    bincoef = m.comb(n,e)
    p = (q**e)*((1-q)**(n-e))
    return p

letters = 'abcdefghijklmnopqrstuvwxyz'

def edit_1(word): #returns a sequence of words that we can obtain by making one mistake 
    n = len(word)
    variations = set()  #add a letter, remove a letter, mispell a letter
    for i in range(n):
        newword = word[:i] + word[(i+1):] #remove the i-th letter
        variations.add(newword)

    for i in range(n+1):
        for letter in letters:
            newword = word[:i] + letter +word[i:] #add a letter
            variations.add(newword)

    for i in range(n):
        for letter in letters:
            if letter != word[i]:
                newword = word[:i] + letter +word[(i+1):] #add a letter
                variations.add(newword)

    for i in range(n-1):
        if word[i] != word[i+1]:
            newword = word[:i] + word[i+1] + word[i] + word [(i+2):]
            variations.add(newword)

    return variations


def edit_k(word,k):
    variations = {word}
    for i in range(k):
        newvariations = set()
        for v in variations:
            newvariations |= edit_1(v) # | represent the union of sets.
        variations = newvariations
    return variations

    
def correct_word (word, maxerrors, q, p_c, words):
    candidates = []
    candidates_1 = []
    for e in range(maxerrors + 1):
        variations = edit_k(word,e)
        for c in variations:
            if ((c in p_c) and (c in words)):
                p_wc = error_prob(e, len(c), q)
                score = p_c[c]*p_wc
                candidate = {'word':c, 'score':score}
                candidates.append(candidate)
    candidates.sort(key=myfunc, reverse=True)
    candidates = candidates[:5]
    for i in range(len(candidates)):
        candidates_1.append(candidates[i]['word'])
    return candidates_1
    

def myfunc(x):
    return x['score']


#p_c = readwords('words.txt')
#candidates = correct_word('pyton', 2,0.01,p_c)
#print(candidates)


    

