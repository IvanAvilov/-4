import json


FILE_NAME = "input.json"


def task() -> float:
    with open(FILE_NAME, 'r') as f:
        list_ = json.load(f)
    result = [i["score"] * i["weight"] for i in list_]
    new_result = sum(result)
    return round(new_result, 3)


print(task())
