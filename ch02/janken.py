import random

OPTIONS = ["グー", "チョキ", "パー"]


def get_human_choice():
    choice_number = int(input("「グー」か「チョキ」か「パー」を番号で選んでください: "))
    return OPTIONS[choice_number - 1]


def get_computer_choice():
    return random.choice(OPTIONS)


def print_result(computer_choice, human_choice):
    beat_mapper = {"グー": "チョキ", "パー": "グー", "チョキ": "パー"}

    human_beat = beat_mapper[human_choice]

    print(f"コンピュータが選んだのは{computer_choice}です")
    print(f"あなたが選んだのは{human_choice}です")

    if computer_choice == human_choice:
        print("引き分けです！")

    elif computer_choice == human_beat:
        print(f"おめでとうございます！ あなたの出した{human_choice}の勝ちです。")

    else:
        print(f"残念でした！ コンピュータの出した{computer_choice}の勝ちです。")


computer_choice = get_computer_choice()
human_choice = get_human_choice()
print_result(computer_choice, human_choice)
