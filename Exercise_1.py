
def duplicate_encode(word):
    small_letter = word.casefold()
    dupi = []
    list_word = []
    for letter in small_letter:
        word_count = small_letter.count(letter)
        if word_count == 1:
            dupi.append("(")
        else:
            dupi.append(")")
    return ("".join(dupi))

word =  "yyRreT"

####### babbal solution
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

enc = duplicate_encode (word)
print (enc)


number = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]

def find_it(seq):
    from collections import Counter
    dict_a = dict(Counter(seq))
    for k,v in dict_a.items():
        if v%2 != 0:
            return (k)


def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

def friend(x):
    fri =[]
    friend = [fri.append(i) for i in x if len(i) == 4]
    return fri
    #Code
fren = ["Ryan", "Kieran", "Mark"]
print (friend(fren))


def validate_pin(pin):
    numbers = [str(i) for i in list(range(0, 10))]
    strpin = [str(i) for i in list(pin)]

    for value in list(strpin):
        if value not in numbers:
            print(value)
            return False
            break
    if len(pin) ==4 or len(pin) ==6:
        return True
    else:
        return False


def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()


print (validate_pin("1212"))

import
