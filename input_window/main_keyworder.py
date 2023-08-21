import pyperclip

from input_window.best_keywords import keywords_opimization
from input_window.checkbox_output import create_checkbox_list
from input_window.new_input_window import create_input_window


def main():
    result = create_input_window()
    good_keywords_str = keywords_opimization(", ".join(result))
    good_keywords_lst = good_keywords_str.split(', ')

    selected_keywords = create_checkbox_list(good_keywords_lst, "Select_keywords")
    rezult_str = ", ".join(selected_keywords)
    pyperclip.copy(rezult_str)
    print(rezult_str)

    return rezult_str


if __name__ == '__main__':
    main()
