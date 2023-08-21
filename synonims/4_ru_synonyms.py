# pip install git+https://github.com/ahmados/rusynonyms.git


from ru_synonyms import SynonymsGraph
import pyperclip

from Common.cvs_writer import save_to_csv
from input_window.checkbox_output import create_checkbox_list

# Initialize both synonyms and antonyms graph
sg = SynonymsGraph()


def get_synonyms(to_word: str) -> dict:
    assert sg.is_in_dictionary(to_word)
    synonyms_list = [synonim for synonim in sg.get_list(to_word)]
    selected_synonyms = create_checkbox_list(synonyms_list, "Select synonims")
    synonyms_str = ", ".join(selected_synonyms)
    save_to_csv([['Main word', 'Synonyms'], [to_word, synonyms_str]],
                '/Users/evgeniy/Documents/keywords/synonyms.csv')
    pyperclip.copy(synonyms_str)
    return selected_synonyms


if __name__ == '__main__':
    print(get_synonyms('коррупция'))
