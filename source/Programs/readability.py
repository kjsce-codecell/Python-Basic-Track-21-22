
letters = 0
words = 1
sentences = 0

input = input("Text: ")

for i in range(len(input)):
    c = input[i]

    if c.isalpha():
        letters += 1

    if c.isspace():
        words += 1

    if c == '.' or c == '?' or c == '!':
        sentences += 1

S = sentences * 100 / words # avg no of sentences per 100 word in a text 

L = letters * 100 / words # average no of letters per 100 words in a text 

output = round(0.0588 * L - 0.296 * S - 15.8) #Coleman-Liau index 

if output < 1:
    print("Before Grade 1")

if output >= 16:
    print("Grade 16+")

if output > 1 and output < 16:
    print("Grade {}" .format(output))