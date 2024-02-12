# importing RegEx python library
import re

# introducing the original string which contains the original text
original_string = """homEwork:
tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""
# creating a variable for string which will further contain the modified text
sentences = ""
# creating the variable for calculating the number of whitespaces
sum_of_whitespaces = 0
# the loop for iterating over characters in the original text
for char in original_string:
    # adding a logic when the character is any kind of whitespaces
    if char.isspace():
        # adding +1 to the total sum of whitespaces
        sum_of_whitespaces+=1

# printing the total count of whitespaces
print("Sum of all whitespaces in the text:", sum_of_whitespaces)

# the loop for interating over the split parts of the original string, which is also being modified:
# we get rid of the tabs and commas. The original text is being split by commas.
for sentence in re.split('\\.',original_string.strip().rstrip('.').replace('\n', '')):
        # creating the variable for holding the value of the modified sentence.
        # In case the sentence contains 'iz' (with whitespaces around it) it is being replaced with 'is'
        # The modified sentence is added to the variable 'sentences'
        sentences += sentence.strip().capitalize().replace(' iz ', ' is ') + ". "
# Creating a variable for holding the value of the last words from each sentence
last_words = ''
# the loop for iterating over each word in the sentences
for word in re.split(' ', sentences):
    # creating the logic for each word that ends with a comma
    if word.endswith('.'):
        # adding the modified last word to the variable last_words
        last_words+=word.rstrip('.') + ' '
# Creating a variable which concatinates both modified text and the sentence with last words
combined_string = sentences.replace('this paragraph.', 'this paragraph. ' + last_words.strip().capitalize() + '.')
# Printing the string with modified text and added a new sentence which consists of the last words of each sentence
print("The final text: " + '\n' + combined_string)

