import pyperclip
from pymystem3 import Mystem

from input_window.best_keywords import keywords_opimization
from input_window.checkbox_output import create_checkbox_list
from input_window.new_input_window import create_input_window
from keyworder.words_more_two_litters import extract_words
from keyworder.write_keywords import write_keywords


def lema(any_text):
    lemmatized_words = extract_words(Mystem().lemmatize(any_text))
    return [word for word in lemmatized_words if len(word) > 2]

def main():
    first_test = create_input_window()[0]
    all_words_list= lema(first_test)
    no_doubles_str = keywords_opimization(", ".join(all_words_list))
    no_doubles_list = no_doubles_str.split(', ')
    selected_words_list = create_checkbox_list(no_doubles_list, "Select!!!")
    selected_words_str = ", ".join(selected_words_list)
    pyperclip.copy(selected_words_str)
    write_keywords(selected_words_str, '/Users/evgeniy/Documents/keywords/keywords in work.txt')


if __name__ == '__main__':
    # print(lema(
    #     'крокодил крокодилов крокодилам Крокодилы динозавриками в аэропорту'))
    main()
