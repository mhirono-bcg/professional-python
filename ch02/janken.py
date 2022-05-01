import random

OPTIONS = ["グー", "チョキ", "パー"]


class JankenSimulator:
    def __init__(self):
        self.computer_choice = None
        self.human_choice = None

    def get_human_choice(self):
        choice_number = int(input("「グー」か「チョキ」か「パー」を番号で選んでください: "))
        self.human_choice = OPTIONS[choice_number - 1]

    def get_computer_choice(self):
        self.computer_choice = random.choice(OPTIONS)

    def print_result(self):
        beat_mapper = {"グー": "チョキ", "パー": "グー", "チョキ": "パー"}

        human_beat = beat_mapper[self.human_choice]

        print(f"コンピュータが選んだのは{self.computer_choice}です")
        print(f"あなたが選んだのは{self.human_choice}です")

        if self.computer_choice == self.human_choice:
            print("引き分けです！")

        elif self.computer_choice == human_beat:
            print(f"おめでとうございます！ あなたの出した{self.human_choice}の勝ちです。")

        else:
            print(f"残念でした！ コンピュータの出した{self.computer_choice}の勝ちです。")

    def simulate(self):
        self.get_computer_choice()
        self.get_human_choice()
        self.print_result()


janken = JankenSimulator()
janken.simulate()
