stroy = ""
previous_word = ""
while True:
    word = input("Please type in a word: ")
    if word == "end" or previous_word == word:
        print(stroy)
        break
    else:
        if len(stroy) == 0:
            stroy = stroy + word    
        else:    
            stroy = stroy + " " + word   
    previous_word = word
    