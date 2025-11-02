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


def sort_on(element):
    return element["num"]


def dic_pair(dictionar):
    ls = []
    for item in dictionar:
        dic = {}
        dic["char"] = item
        dic["num"] = dictionar[item]
        ls.append(dic)
    ls.sort(reverse=True, key=sort_on)
    return ls
