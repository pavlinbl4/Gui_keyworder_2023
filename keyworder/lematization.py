import pyperclip
from pymystem3 import Mystem

from Common.write_keywords import write_keywords
from KW_2023_08.best_keywords import keywords_optimization
from KW_2023_08.checkbox_output import create_checkbox_list
from KW_2023_08.new_input_window import create_input_window
from Common.only_words_from_string import extract_words_no_digits


# automate text to keyword optimizator
def lema_minus_bad_words(any_text: str):
    all_words_list = lema(any_text)
    return keywords_optimization(", ".join(all_words_list))


def lema(any_text: str) -> list:
    lemmatized_words_lst = extract_words_no_digits(Mystem().lemmatize(any_text))
    return [word for word in lemmatized_words_lst if len(word) > 2]


def main():
    first_test = create_input_window("Input your text for lemmatization")[0]
    all_words_list = lema(first_test)
    no_doubles_str = keywords_optimization(", ".join(all_words_list))
    no_doubles_list = no_doubles_str.split(', ')
    selected_words_list = create_checkbox_list(no_doubles_list, "Select!!!")
    selected_words_str = ", ".join(selected_words_list)
    pyperclip.copy(selected_words_str)
    write_keywords(selected_words_str, '/Users/evgeniy/Documents/keywords/keywords in work.txt')


if __name__ == '__main__':
    print(lema_minus_bad_words(
        'крокодил крокодилов крокодилам Крокодилы динозавриками в аэропорту _РУССКИЙ ты для'))
    # main()
