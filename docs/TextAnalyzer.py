name = input("Enter full name: ")
sentence = input("Enter a sentence or short paragraph: ")
print("My name is " + format(name) + ""
"and I attend school at: " + format(sentence))
search_pharse = input("Enter a word/pharse to search in the sentence: ")

sentence_title = sentence.title()
print("The sentence is the title: " + sentence_title)

sentence_upper = sentence.upper()
print("The sentence is in uppercase: " + sentence_upper)

sentence_lower = sentence.lower()
print("The sentence is in lowercase " + sentence_lower)

sentence_strip = sentence.strip("")
print("The sentence is stripped of spaces: " + sentence_strip)

sentence_replace = sentence.replace("s","z")
print("The sentence will replace something: " + sentence_replace)

sentence_split = sentence.split()
print("The sentence will split: " + str(sentence_split))

sentence_length = len(sentence)
print("The sentences length will be shown: " + str(sentence_length))

sentence_endswith = sentence.endswith("bye")
print("The sentence will end with: " + str(sentence_endswith))

sentence_startswith = sentence.startswith("hi")
print("The sentence will start with: " + str(sentence_startswith))

sentence_isalpha = sentence.isalpha()
print("The sentence has alphabets: " + str(sentence_isalpha))
