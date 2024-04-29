import nltk
nltk.download('stopwords')
import re
from collections import Counter

# Function to read the contents of the text file
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to remove stop words from the text
def remove_stopwords(text):
    try:
        # Check if NLTK stopwords are available, if not, download them
        nltk.data.find('corpora/stopwords.zip')
    except LookupError:
        nltk.download('stopwords')

    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    words = re.findall(r'\b\w+\b', text.lower())
    return [word for word in words if word not in stop_words]

# Function to count the frequency of each word
def count_word_frequency(words):
    return Counter(words)

# Function to display word frequency count to the console
def display_word_frequency(word_freq):
    for word, freq in word_freq.items():
        print(f'{word}: {freq}')

# Main function
def main():
    # Path to the text file
    file_path = 'random_paragraphs.txt'
    
    # Read the contents of the text file
    text = read_file(file_path)
    
    # Remove stop words from the text
    words = remove_stopwords(text)
    
    # Count the frequency of each word
    word_freq = count_word_frequency(words)
    
    # Display word frequency count to the console
    display_word_frequency(word_freq)

if __name__ == "__main__":
    main()
