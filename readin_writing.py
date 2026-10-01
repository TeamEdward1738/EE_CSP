# EE, Reading and writing to files

with open('practice.txt', "r") as file:
    content = file.read()
    print(content)
    word = content.find("sugar free bananas are reallllll!!!")
    length = len("sugar free bananas are reallllll!!!")
    print(content[word:word+length])
    print(content.upper())
    content += " Treyson!"
    file.write(content)

with open("practice.txt", "a") as file:
    file.write("another line")