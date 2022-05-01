# 段落を文とトークンに分割。単純なコードの列
import re  # https://docs.python.org/ja/3/howto/regex.html参照


def get_matches_for_pattern(pattern, sentence):
    matches = pattern.findall(sentence)
    return [match[0] for match in matches]


product_review = """This is a fine milk, but the product line appears
 to be limited in available colors. I could only find white."""  # <1>

sentence_pattern = re.compile(r"(.*?\.)(\s|$)", re.DOTALL)  # <2>
sentences = get_matches_for_pattern(sentence_pattern, product_review)

word_pattern = re.compile(r"([\w\-']+)([\s,.])?")  # <5>
for sentence in sentences:
    words = get_matches_for_pattern(word_pattern, sentence)
    print(words)
