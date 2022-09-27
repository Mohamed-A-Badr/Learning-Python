def translate(string):
    translation = ""
    for char in string:
        if char.lower() in "aeiou":
            if char.isupper():
                translation = translation + "Z"
            elif char.islower():
                translation = translation + "z"
            else:
                translation = translation + char
        else:
            translation = translation + char
    return translation


print(translate(input("Enter your statement: ")))
