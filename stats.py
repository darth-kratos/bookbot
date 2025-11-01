def word_count(book):
    return len(book.split())


def char_count(text):
    text = text.lower()
    dic = {}

    for i in text:
        if i not in dic:
            contor = 0
            for j in text:
                if i == j:
                    contor += 1
            dic[i] = contor

    return dic
