def _join_names(names):
    name_string = ""
    for index, name in enumerate(names):  # namesの各要素をループ
        if index > 0:
            name_string += "に"
        if index == len(names) - 1:
            name_string += "、それから"
        name_string += name
    return name_string


def print_movie_title(title: str, sanbaka_names: list[str]):
    print(f"{title}: {_join_names(sanbaka_names)}")


print_movie_title("Three Idiots: ", ["ラリー", "カーリー", "モー"])


# # 最初のバージョン
# names = ['ラリー', 'カーリー', 'モー']
# message = '三ばか大将：'
# for index, name in enumerate(names): # namesの各要素をループ
#     if index > 0:
#         message += 'に'
#     if index == len(names) - 1:
#         message += '、それから'
#     message += name
# print(message)
