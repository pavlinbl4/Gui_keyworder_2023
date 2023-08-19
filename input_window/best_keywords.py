import re
from input_window.bad_words_from_file import get_bad_words_from_txt_file

# words_to_remove = r'_РЕЛИГИЯ|_гипермаркеты|_фирмы|_ПРЕДМЕТ_|_People|_ГОРОДА И СТРАНЫ_|_PERSONS|_CITY|_ИМЯ СОБСТВЕННОЕ_|COUNTRY|_РУССКИЙ_|_ГОРОДА И СТРАНЫ|\|'


# def add_words_to_txt(path_to_txt):  # temp function to add words to file
#     with open(path_to_txt, 'a') as txt_file:
#         for i in words_to_remove.lstrip().split('|'):
#             # txt_file.writelines(words_to_remove.lstrip().split('|'))
#             if len(i) > 2:
#                 txt_file.write(i + '\n')


def keywords_opimization(string, path_to_bad_words_file='/Users/evgeniy/Documents/keywords/bad_words.txt'):
    words_to_remove = get_bad_words_from_txt_file(path_to_bad_words_file)

    # remove bad words
    no_bad_words = re.sub(words_to_remove, "", string).strip()

    # remove doubles
    cleaned_string = re.sub(r'\b(\w+)\b(?=.*\b\1\b)', r'', no_bad_words)

    # Remove all punctuation except commas
    cleaned_string = re.sub(r'(?<!\w)[^\w\s,-]|[^\w\s,-](?!\w)', '', cleaned_string)

    # Extract words and separate with commas
    words = re.findall(r'\b[\w-]+\b', cleaned_string)
    result = ', '.join(words)

    # set limit of keywords
    while len(result) > 500:
        del words[-1]
        result = ', '.join(words)

    return result


