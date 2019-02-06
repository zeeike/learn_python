###
# Giraffe Language 
#vowels -> g
#----------------
#
#dog -> dgg
#cat -> cgt
###


def translate(phrase):
    result = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                result = result + "G"
            else:
                result = result + "g"
        else:
            result = result + letter
    return result

#print(translate("dog"))

print(translate(input("Enter a phrase to translate:")))