def pig_it(text):
    #your code here
    first_char = ""
    rest_of_word = ""
    translated = []
    sentence = text.split(" ")
    for word in sentence:
        first_char = str(word[0])
        rest_of_word = str(word[1:])
        if first_char.isalpha():
            first_char += "ay"
        translated.append(rest_of_word+first_char)
    return(str(" ".join(translated)))
