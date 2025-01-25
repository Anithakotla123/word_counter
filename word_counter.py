def count_words():
    user_input = input("Enter a sentence or paragraph: ").strip()
    
    # Error handling for empty input
    if not user_input:
        print("Error: No input provided. Please enter some text.")
        return
    
    # Splitting the input into words and counting them
    words = user_input.split()
    word_count = len(words)
    
    # Display the word count
    print(f"The number of words in the input is: {word_count}")


# Call the function
if __name__ == "__main__":
    count_words()
