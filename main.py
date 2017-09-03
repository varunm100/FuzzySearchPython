import re, itertools
from itertools import chain, combinations, product, groupby

global counter
counter = 0

def hamming_circle(s, n, alphabet):
    global counter
    for positions in combinations(range(len(s)), n):
        for replacements in product(range(len(alphabet) - 1), repeat=n):
            cousin = list(s)
            for p, r in zip(positions, replacements):
                counter+=1
                if cousin[p] == alphabet[r]:
                    cousin[p] = alphabet[-1]
                else:
                    cousin[p] = alphabet[r]
            yield ''.join(cousin)

def hamming_ball(s, n, alphabet):
    return chain.from_iterable(hamming_circle(s, i, alphabet)
                               for i in range(n + 1))
def GetConsDupli(iString):
    global counter
    counter+=len(iString)
    return str(''.join(i for i, _ in itertools.groupby(str(iString))))

def remove(s, indx):
    global counter
    counter += 1
    NewString = ''
    if indx != (len(s)-1):
        NewString = s[:indx] + s[(indx+1):]
    else:
        NewString = s[:indx]
    return NewString

def GetFuzzyStr(inputStr, dis):
    global counter
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    vowels = ['a','e','i','o','u','y']
    NDupli = GetConsDupli(inputStr)
    dupli = False

    if NDupli == inputStr:
        dupli = False
    else:
        dupli = True
    AllHamDis = list(hamming_ball(inputStr, dis, alphabet))
    if dupli:
        AllHamDis.extend(list(hamming_ball(NDupli, dis, alphabet)))
    for letter in alphabet:
        counter+=1
        AllHamDis.append(str(inputStr + letter))
    if dupli:
        for letter in alphabet:
            counter+=1
            AllHamDis.append(str(NDupli + letter))
    for index in range((len(inputStr))):
        counter+=1
        AllHamDis.append(remove(inputStr, index))

    for index in range((len(inputStr))):
    	for letter in alphabet:
    		List = []
    		List.append(letter)
    		List = inputStr[:index] + List[0] + inputStr[index:]
    		AllHamDis.append(List)

    FinalArr = []
    for Search in AllHamDis:
        counter+=1
        FinalArr.append(Search.lower())

    return set(FinalArr)

PeopleSet = set()
PeopleSet.add("varun")
PeopleSet.add("varan")
PeopleSet.add("raji")
PeopleSet.add("raju")
PeopleSet.add("rajj")
PeopleSet.add("rajy")
PeopleSet.add("raju")
PeopleSet.add("aakash")
PeopleSet.add("akashy")
PeopleSet.add("akaashy")
PeopleSet.add("raman")
PeopleSet.add("ramenyany")

def main(TargetName, SearchLen):
    global counter
    FuzzySearches = GetFuzzyStr(TargetName, SearchLen)
    print(str(FuzzySearches) + '\n')
    for Search in FuzzySearches:
        if Search in PeopleSet:
            print(Search + " : " + TargetName)
    print("# of Fuzzy Strings Found: " + str(len(FuzzySearches)))
    print(str(counter) + " operations done!")
    print('\n')

main('akash',1)
main('varun',1)
#main('rajb', 2)
#main('raj', 2)
#main('rajj', 2)