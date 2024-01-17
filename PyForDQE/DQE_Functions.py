#HW2

# creating the list with 2 dictionaries
original_list = [{'a': 16, 'b': 16, 'c': 34, 'i' : 1}, {'a': 15, 'b': 56, 'd': 18, 'c': 78}]

# creating the new empty dictionary
new_dict = {};

# Creating the function for combining two dictionaries for the list
def combine_two_dictionaries(list_with_dictionaries):
  # the loop for inerating over each dictionary
  for i in range(len(list_with_dictionaries)-1):
    # creating the set consisting of common keys from 1st and 2d dictionary
    common_keys = set(list_with_dictionaries[i].keys()) & set(list_with_dictionaries[i + 1].keys())
    # the loop for iterating keys from the set of common keys
    for key in common_keys:
        # checking if the value of the key from 1st dictionary is bigger then the value from the 2d dictionary
        if list_with_dictionaries[i][key] > list_with_dictionaries[i+1][key]:
            # if the value of the key from 1st dictionary is bigger that it is added to the new dictionary
            new_dict[key] = list_with_dictionaries[i][key]
        # the logic for the rest of the keys
        else:
            # the value of the key from 2d dictionary is added to the new dictionary
            new_dict[key] = list_with_dictionaries[i+1][key]
    # creating the set with unique keys from 1st dictionary
    unique_keys1 = set(list_with_dictionaries[i].keys()) - common_keys
    # the loop for iterating unique keys from 1st dictionary
    for key in unique_keys1:
        # adding the unique key and value from the 1st dictionary to the new dictionary
        new_dict[key] = list_with_dictionaries[i][key]
    # creating the set with unique keys from 2d dictionary
    unique_keys2 = set(list_with_dictionaries[i+1].keys()) - common_keys
    # the loop for iterating unique keys from 2d dictionary
    for key in unique_keys2:
        # adding the unique key and value from the 2d dictionary to the new dictionary
        new_dict[key] = list_with_dictionaries[i+1][key]
# printing the new dictionary with unique keys and values from both dictionaries and filtered common keys
    return new_dict

print("The function for combining two dictionaries is called: ", combine_two_dictionaries(original_list))


#HW3
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

# Creating a function for counting whitespaces
def count_whitespaces(string):
    # creating a local variable for the total sum of whitespaces
    sum = 0
    # the loop for iterating over characters in the original text
    for char in string:
    # adding a logic when the character is any kind of whitespaces
      if char.isspace():
        # adding +1 to the total sum of whitespaces
          sum+=1
    return sum

# printing the total count of whitespaces
print("Funtion for counting whitespaces sum in the text is called:", count_whitespaces(original_string))

# Creating a function for modifying original string
def modify_text(text):
   # creating a variable for string which will further contain the modified text
    global sentences
   # the loop for interating over the split parts of the original string, which is also being modified:
   # we get rid of the tabs and commas. The original text is being split by commas.
    for sentence in re.split('\\.',text.strip().rstrip('.').replace('\n', '')):
        # creating the variable for holding the value of the modified sentence.
        # In case the sentence contains 'iz' (with whitespaces around it) it is being replaced with 'is'
        # The modified sentence is added to the variable 'sentences'
        sentences += sentence.strip().capitalize().replace(' iz ', ' is ') + ". "
    return sentences

print("The function for modifying text is called:", modify_text(original_string))

# Creating a function for making a sentence from the last word of each sentence in the text
def creating_sentence_from_last_words(list_of_sentences):
    # Creating a variable for holding the value of the last words from each sentence
    last_words = ''
    # the loop for iterating over each word in the sentences
    for word in re.split(' ', list_of_sentences):
      # creating the logic for each word that ends with a comma
      if word.endswith('.'):
        # adding the modified last word to the variable last_words
        last_words+=word.rstrip('.') + ' '
    return last_words

# Creating a function for adding the new sentence to the original text
def adding_new_sentence():
     # Creating a variable which concatinates both modified text and the sentence with last words
     combined_string = sentences.replace('this paragraph.', 'this paragraph. ' + creating_sentence_from_last_words(sentences).strip().capitalize() + '.')
     # Printing the string with modified text and added a new sentence which consists of the last words of each sentence
     return '\n' + combined_string
# Printing the finalized string
print("The function for adding a sentence to the text is called and the final text is displayed:", adding_new_sentence())