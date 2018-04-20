sentence = input("Enter your sententce to inflate:  ")
# print("this is your string", sentence)

words = sentence.split(' ')
# print("this is an array", words)

# indecies = [] #to ignore the values that have already been replace

wordsToFind = [['zero', 'none', 'nil', 'null'],
    ['one', 'won', 'juan'],
    ['two', 'to', 'too', 'tu'],
    ['three'],
    ['four', 'for', 'fore'],
    ['five'],
    ['six'],
    ['seven'],
    ['eight', 'ate'],
    ['nine'],
    ['ten'],
    ['eleven'],
    ['twelve', 'dozen'],
    ['never'],
    ['half'],
    ['once'],
    ['twice'],
    ['single'],
    ['double'],
    ['first'],
    ['second'],
    ['third'],
    ['fourth', 'forth']]


wordsInflateTo =['one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'once',
    'one and a half',
    'twice',
    'thrice',
    'double',
    'triple',
    'second',
    'third',
    'fourth',
    'fifth'
    ]


for index, word in enumerate(words): # to loop over words in sentences
    # if index in indecies:
    #     print("Already replaced", index, word)
    #     continue

    # else :
    #     print("you are awesome ", word, index)
    #     # words[index]= word.replace(a, "one")  
    if word.isdigit():
        words[index] = str(int(word)+1)
        continue 

    for index2, inflateWords in enumerate(wordsToFind):
        word = word.lower();
        # if any(x in word for x in inflateWords): # to find if a word exists that needs to be inflated
        for match in inflateWords:
            if match in word:
                words[index]= word.replace(match, wordsInflateTo[index2])
                # indecies.append(index)
        

print("Your inflated sentence is:       ", " ".join(words))
            