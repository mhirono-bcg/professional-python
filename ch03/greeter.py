import datetime
import locale

# change the locale
locale.setlocale(locale.LC_TIME, "ja_JP.UTF-8")


def _day():
    day = datetime.datetime.now().strftime("%A")
    return day


def _part_of_day():
    hour = datetime.datetime.now().hour
    if hour <= 12:
        part = "午前"
    elif hour > 12 and hour <= 17:
        part = "午後"
    else:
        part = "夜"
    return part


# Greeter class knows too much
# Refactor the methods relevant to date out of this class
class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self, store):
        day = _day()
        part = _part_of_day()
        print(f"{store}へようこそ！私、{self.name}と申します。")
        print(f"{day}の{part}、いかがお過ごしですか？")
        print(f"本日のお客様に20% OFFのクーポンを差し上げます！")


Greeter(name="廣野").greet(store="イオンレイクタウン店")
