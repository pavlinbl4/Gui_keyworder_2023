import pyperclip

from KW_2023_08.best_keywords import keywords_optimization
from KW_2023_08.checkbox_output import create_checkbox_list
from KW_2023_08.new_input_window import create_input_window


def main() -> str:
    result = create_input_window("Enter text here")

    if result == []:
        quit()

    good_keywords_str = keywords_optimization(", ".join(result))
    good_keywords_lst = good_keywords_str.split(', ')

    selected_keywords = create_checkbox_list(good_keywords_lst, "Select_keywords")
    rezult_str = ", ".join(selected_keywords)
    pyperclip.copy(rezult_str)
    print(rezult_str)

    return rezult_str


if __name__ == '__main__':
    main()
