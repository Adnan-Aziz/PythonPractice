import string

EtoH = {'bread':'paroti', 'wine':'sharab', 'with':'saath', 'I':'Mein',
'eat':'khana', 'drink':'peena', 'John':'Jaan',
'friends':'dost', 'and': 'aur', 'of':'ka','red':'laal','good':'acha'}
HtoE = {'paroti':'bread', 'sharabn':'wine', 'saath':'with', 'Mein':'I',
'khana':'eat', 'peena':'drink', 'Jaan':'John',
'dost':'friends', 'aur':'and', 'ka':'of', 'laal':'red'}

dicts = {'English to Hindi':EtoH, 'Hindi to English':HtoE}

def translateWord(word,dictionary):
    if word in dictionary.keys() :
        return dictionary[word]
    elif word !='' :
        return '"' + word + '"'
    return word

def translate(phrase,dicts,direction) :
    letters = string.ascii_uppercase + string.ascii_lowercase
    dictionary = dicts[direction]
    translation = ''
    word = ''
    for c in phrase : 
        if c in letters : 
            word = word + c
        else :
            translation += translateWord(word,dictionary) + c
            word=''
    return translation + ' ' + translateWord(word,dictionary) + c

print( "{0}".format(translate('I drink good red wine, and eat bread.',
dicts,'English to Hindi')))  
