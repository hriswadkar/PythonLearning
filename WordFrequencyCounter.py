# This program accepts a sentence from the user and counts the frequency of each word in the sentence.
def count_word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    for word in words:
        word = word.lower()  # Convert to lowercase for case-insensitive counting
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def main():
    print("This program counts the frequency of each word in a sentence.")
    input_sentence = input("Enter a sentence: ")
    word_frequency = count_word_frequency(input_sentence)
    print("Word Frequency:")
    for word, count in word_frequency.items():
        print(f"{word}: {count}")
        
if __name__ == "__main__":
    main()