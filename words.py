def print_upper_words(words,must_start_with):
    """This function takes a list of words and prints
    only the words that start with the provided letters"""
    for word in words:
        for start_letter in must_start_with:
            if(word.startswith(start_letter)):
                print(word)
                break

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
