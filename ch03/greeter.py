import datetime
import locale

# change the locale
locale.setlocale(locale.LC_TIME, "ja_JP.UTF-8")


class Greeter:
    def __init__(self, name):
        self.name = name
        self.day = None
        self.part = None

    def _day(self):
        self.day = datetime.datetime.now().strftime("%A")

    def _part_of_day(self):
        hour = datetime.datetime.now().hour
        if hour <= 12:
            self.part = "午前"
        elif hour > 12 and hour <= 17:
            self.part = "午後"
        else:
            self.part = "夜"

    def greet(self, store):
        self._day()
        self._part_of_day()
        print(f"{store}へようこそ！私、{self.name}と申します。")
        print(f"{self.day}の{self.part}、いかがお過ごしですか？")
        print(f"本日のお客様に20% OFFのクーポンを差し上げます！")


Greeter(name="廣野").greet(store="イオンレイクタウン店")
