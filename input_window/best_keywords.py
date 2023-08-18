import re

words_to_remove = r'_РЕЛИГИЯ|_гипермаркеты|_фирмы|_ПРЕДМЕТ_|_People|_ГОРОДА И СТРАНЫ_|_PERSONS|_CITY|_ИМЯ СОБСТВЕННОЕ_|COUNTRY|_РУССКИЙ_|_ГОРОДА И СТРАНЫ|\|'


def keywords_opimization(string):
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
