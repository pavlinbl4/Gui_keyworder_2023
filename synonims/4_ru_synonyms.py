# pip install git+https://github.com/ahmados/rusynonyms.git


from ru_synonyms import SynonymsGraph
import pyperclip

from Common.cvs_writer import save_to_csv
from KW_2023_08.checkbox_output import create_checkbox_list
from KW_2023_08.new_input_window import create_input_window

# Initialize both synonyms and antonyms graph
sg = SynonymsGraph()


def get_synonyms(to_word: str) -> list:
    assert sg.is_in_dictionary(to_word)
    synonyms_list = [synonim for synonim in sg.get_list(to_word)]
    selected_synonyms = create_checkbox_list(synonyms_list, "Select synonyms")
    synonyms_str = ", ".join(selected_synonyms)
    save_to_csv([[to_word, synonyms_str]],
                '/Users/evgeniy/Documents/keywords/synonyms.csv')
    pyperclip.copy(synonyms_str)
    return selected_synonyms


def main():
    to_word = create_input_window("Enter word")[0]
    get_synonyms(to_word)


if __name__ == '__main__':
    # print(get_synonyms('бизнесмен'))

    main()
