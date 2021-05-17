"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    evennums = []

    for num in nums:
        if num % 2 == 0:
            evennums.append(num)

    return evennums

def get_odd_indices(items):
    result = []

    for i in range(len(items)):
        if i % 2 != 0:
            result.append(items[i])

    return result


def print_as_numbered_list(items):
    
    i = 1

    for item in items:
        print(f"{i}. {item}")

        i += 1


def get_range(start, stop):
    nums = []

    num = start
    while num < stop:
        nums.append(num)
        num += 1
    


def censor_vowels(word):

    chars = []

    for letter in word:
        if letter in "aeiou":
            chars.append("*")
        else:
            chars.append(letter)
    
    return "".join(chars)


def snake_to_camel(string):
    camelcase = []

    for word in string.split("_"):
        camelcase.append(f"{word[0].upper}{word[1:]}")

    return "".join(camelcase)


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
