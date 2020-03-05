# The program outputs the text in reverse

text = input('Enter text\n')

while text:
    print(text[-1], end='')
    text = text[:-1]

