import json
import random

FOODS = ["ピザ", "ハンバーガー", "サラダ", "スープ"]


def to_json(food):
    return json.dumps({"food": food})


def to_xml(food):
    return f"<response><food>{food}</food></response>"


def get_format_function(accept=None):
    formats = {"application/json": to_json, "application/xml": to_xml}
    return formats.get(accept, None)


def random_food(request):
    food = random.choice(FOODS)
    format_function = get_format_function(request.headers.get("Accept"))
    return format_function(food)
