from ruwordnet import RuWordNet


def get_(to_word):
    wn = RuWordNet()
    return [x.synset.title.lower() for x in wn.get_senses(to_word)]


if __name__ == '__main__':
    print(get_('ключ'))
