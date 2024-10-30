"""Personalised Greeting Creator."""
# Import the random module
import random as ra

greetings = ["Hey {}, I hope you are well!",
             "Whassup {}!",
             "Have a most splendid day {}"]
# range 1 - max of dictionary size
dictionary_size = range(1, len(greetings)+1)
# combine together the greetings and dictionary;zip=combine together (,)
greetings_dict = dict(zip(dictionary_size, greetings))

def choose_random_greeting_template()-> str:
    """Return a random template string from the greetings dictionary.
    """
    random_key = ra.choice(dictionary_size)
    return greetings_dict[random_key]


def choose_greeting_template()-> str:
    """Return a template string from the greetings dictionary.
    """
    try:
        choice = int(input(f"Choose an integer between 1 & {max(dictionary_size)}: "))
        greeting = greetings_dict[choice]
    except ValueError:
        print("Invalid input")
    except KeyError:
        print("Invalid Key!")
    else:
        return greeting
    finally:
        return choose_random_greeting_template()


def write_to_file(content, file_name="greeting.txt", mode="w") -> None:
    if content:
        with open(file_name, mode) as my_file:
            my_file.write(content + "\n")
        print(f"Greeting written to {file_name}")
    else:
        print("No content to write")


def parse_contents(content: str)-> list:
    """ Parses the content into words and returns a list of words. """
    # split the greeting into individual words
    return content.split()


def build_frequency_dict(words:list) -> dict:
    """ Takes a list of words and returns a dictionary with the word frequencies."""
    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    return frequency_dict


def print_frequencies(frequency_dict: dict) -> None:
    """ Prints the word frequencies from the dictionary."""
    for word, frequency in frequency_dict.items():
        print(f"'{word}': {frequency} time(s)")


def run_all() -> None:
    """ Driver function to control flow, generate a greeting, write it to a file, and show word frequencies."""
    name = input("Enter your name: ")
    if not name:
        print("No name entered")
        return

    try:
        greeting_style = int(input("Enter 1 for random greeting, or 2 to choose! "))
    except ValueError:
        print(f"{name.title()}, you entered an invalid choice.")
        return

    final_greeting = ""
    if greeting_style == 1:
        random_greeting = choose_random_greeting_template()
        final_greeting = random_greeting.format(name.title())
    elif greeting_style == 2:
        selective_greeting = choose_greeting_template()
        final_greeting = selective_greeting.format(name.title())
    else:
        print(f"You didn't enter 1 or 2, {name.title()}... ")
        return
    # Step 1: print the final greeting
    print("Final Greeting:", final_greeting)

    # Step 2: Write the greeting to a file
    write_to_file(final_greeting)

    # Step 3: Parse the content into words
    parsed_words = parse_contents(final_greeting)

    # Step 4: Build the word frequency dictionary
    word_frequencies = build_frequency_dict(parsed_words)

    # Step 5: Print word frequencies
    print_frequencies(word_frequencies)

# Run the function
run_all()