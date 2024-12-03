# Dynamic Frequency Harmonizer System

def calculate_harmonic_frequency(word):
    """
    Calculate the harmonic frequency of a word.
    The frequency is the sum of the ASCII values of each letter,
    multiplied by the length of the word.
    """
    return sum(ord(char) for char in word) * len(word)

def dynamic_frequency_harmonizer():
    """
    Main function to analyze words entered by the user
    and display the top 3 words with the highest harmonic frequency.
    """
    print("Welcome to the Dynamic Frequency Harmonizer System!")
    print("Enter a list of words (separated by spaces):")
    
    # Get input from the user
    words = input("Words: ").split()
    
    # Calculate frequencies for each word
    word_frequencies = {word: calculate_harmonic_frequency(word) for word in words}
    
    # Sort words by frequency in descending order
    sorted_words = sorted(word_frequencies.items(), key=lambda item: item[1], reverse=True)
    
    # Display the top 3 results
    print("\nTop 3 words by harmonic frequency:")
    for i, (word, frequency) in enumerate(sorted_words[:3], start=1):
        print(f"{i}. {word} - Frequency: {frequency}")

if __name__ == "__main__":
    dynamic_frequency_harmonizer()
