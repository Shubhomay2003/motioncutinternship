#!/usr/bin/env python
# coding: utf-8

# In[6]:


import re # importing re(regular expression) library
def count_words(text):
    """
    This function counts the number of words in the given text.
    Words are assumed to be separated by whitespace.
    
    Parameters:
    text (str): The input text to be analyzed.
    
    Returns:
    int: The number of words present in the input text.
    """
    # Use regular expressions to replace punctuations with null character
    text = re.sub(r'[^\w\s]', '', text)# it ignores any word character and whitespaces and hence selects special characters and substitutes with null character
    # Split the text by whitespace to get words and filter out any empty strings
    words = text.split()
    return len(words)

def main():
    """
    Prompts the user for input, counts the words, and displays the count.
    """
    w_input = input("Enter a sentence or paragraph: ").strip()# here strip() eliminates extra whitespaces present at first and last of input text
    
    # Checking if the input is empty 
    if not w_input:
        print("Sorry, the input cannot be empty!!!! Please try again.")
        return
    
    # Count the number of words in the input
    word_count = count_words(w_input)
    
    # Display the word count to the console
    print(f"The number of words present in the entered text is: {word_count}")

if __name__ == "__main__":
    main()


# In[ ]:




