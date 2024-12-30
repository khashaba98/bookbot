def count_words(text):
    """
    Counts the number of words in the given text.
    :param text: The text of the book as a string.
    :return: The number of words in the text.
    """
    words = text.split()
    return len(words)


def count_characters(text):
    """
    Counts the frequency of each character in the text.
    :param text: The text of the book as a string.
    :return: A dictionary with characters as keys and their frequencies as values.
    """
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count


def print_report(file_path, word_count, char_count):
    """
    Prints a formatted report of the word and character counts.
    :param file_path: Path to the book file.
    :param word_count: The total word count of the book.
    :param char_count: A dictionary with character frequencies.
    """
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")

    # Convert character counts to a sorted list
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    # Print each character's frequency
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")


def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    print_report(path_to_file, word_count, char_count)


if __name__ == "__main__":
    main()
