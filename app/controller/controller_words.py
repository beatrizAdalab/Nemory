from ..models import Word, word_schema


def get_all_words():
    words = Word.get_all()
    return word_schema.dump(words, many=True)


def get_filter_words(key, value):
    data = Word.get_filter_all(key, value)
    words = word_schema.dump(data, many=True)

    if words:
        return words
    else:
        return "incorrect parameters: You must enter a valid filter"


def get_filter_word(key, value):
    data = Word.get_filter_one(key, value)
    word = word_schema.dump(data)

    if word:
        return word
    else:
        return "incorrect parameters: You must enter a valid filter"
