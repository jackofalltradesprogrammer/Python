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


#  InflationaryLanguage: 
# The comedian Victor Borge used to perform a comedy routine called ”Inflationary
# Language” in many of his performances. He observed that many words
# contain numbers and despite what the economy does, the language never keeps
# up with the increases. He suggested that words like WONderful should become
# TWOderful, beFORE should be beFIVE, and so FIFTH, I mean so FORTH.
# Though the English language has far too many words for us to do this in any
# simple way, you are only responsible for making the conversions shown in the
# table below. Also, if the string contains an integer it must also be increased
# by 1. You may use any technique you feel is appropriate however keep in mind
# that the user can input a string of any valid length and that your solution
# should NOT be case sensitive. Your output should exactly match the sample
# outputs. For full marks put all your inflation logic inside an appropriate number
# of modules.
# Words you need to inflate:
# When you find Inflate it to
# zero, none, nil, null one
# one, won, Juan two
# two, to, too, tu three
# three four
# four, for, fore five
# five six
# six seven
# seven eight
# eight, ate nine
# nine ten
# ten eleven
# eleven twelve
# twelve, dozen thirteen
# never once
# half one and a half
# once twice
# twice thrice
# single double
# double triple
# first sec
# Sample program runs:
# Enter your sentence to inflate: I wonder.
# Your inflated sentence is: I twoder.
# Enter your sentence to inflate:
# Your inflated sentence is:
# Enter your sentence to inflate: It was the best of times.
# Your inflated sentence is: It was the best of times.
# Enter your sentence to inflate: A Tale of 2 Cities
# Your inflated sentence is: A Tale of 3 Cities
# Enter your sentence to inflate: I WoNder if 18 is bigger than 1919191?
# Your inflated sentence is: I twoder if 19 is bigger than 1919192?
            