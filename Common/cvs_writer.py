import os
import csv


def save_to_csv(data: list, file_path: str):
    folder = os.path.dirname(file_path)
    if not os.path.exists(folder):
        os.makedirs(folder)
    if not os.path.exists(file_path):
        print('Enter columns name separated with comma')
        columns_names = input()
        data.insert(0,columns_names.split(','))

    with open(file_path, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)


if __name__ == '__main__':
    save_to_csv([['Name', 'Age', 'eee'], ['John', 20], ['Jane', 25]],
                '/Users/evgeniy/Documents/slon/testw3.csv')
