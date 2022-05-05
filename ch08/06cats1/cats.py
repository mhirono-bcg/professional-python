class BigCat:
    def eats(self):
        return ["齧歯動物"]


class Lion(BigCat):
    def eats(self):
        return ["ヌー"]


class Tiger(BigCat):
    def eats(self):
        return ["水牛"]


class Liger(Lion, Tiger):
    def eats(self):
        return super.eats() + ["ウサギ", "牛", "豚", "鶏"]


if __name__ == "__main__":
    lion = Lion()
    print("ライオンが食べるもの：", lion.eats())
    tiger = Tiger()
    print("虎が食べるもの：", tiger.eats())
    liger = Liger()
    print("ライガーが食べるもの：", liger.eats())
