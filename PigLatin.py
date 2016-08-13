# The Piglatin Translator
print ("Welcome to the Pig Latin Translator")
word = input("Enter the word you would like to translate: ")
if len(word) > 0 and word.isalpha():
    dank = "ay"
    lowercase = word.lower()
    firstletter = lowercase[0]
    new_word = word[1:len(word)]
    final_word = new_word + firstletter + dank
    print ("Pig Latin: ", final_word)
else:
    print ("empty")
input("Press Enter to exit")
