import json
import re
from typing import List, Union


def parse_tasks_text(text: str) -> List[str]:
    res = re.sub("\n+", " ", text.strip())

    number = 1
    sentences = []
    while True:
        try:
            sentence = re.search(rf"{number}\.(.*?) {number + 1}\.", res).group(1)
        except AttributeError:
            sentence = re.search(rf"{number}\.(.*)", res).group(1)
            sentences.append(sentence)
            break
        else:
            sentences.append(sentence)
            number += 1

    sentences = [
        re.sub(r"^\. ", "", s.replace("...", "_").strip())
        for s in sentences
    ]

    return sentences


def parse_exercise(exercise_text: str, parse_exercise_text: bool = True) -> dict:
    """
    Парсит текст упражнения в объектик: {exercise_number, exercise_text, tasks}

    :param exercise_text: Текст упражнения
    :param parse_exercise_text:
        В результате парса, получаем словарик с ключом {exercise_text} - это текст упражнения, например:
        Вставьте одно из следующих слов: some, any, по, the, а или оставьте пропуски незаполненными.
        Если {parse_exercise_text} = True, то {exercise_text} будет парсится, иначе нет
    :return: Объектик
    """
    text = exercise_text.strip().split("\n", 2 if parse_exercise_text else 1)
    res = {
        'exerciseNumber': int(re.search(r"Упражнение\s+(\d+)", text[0]).group(1)),
        'tasks': parse_tasks_text(text[-1])
    }
    if parse_exercise_text:
        res['exerciseText'] = text[1]

    return res


def json_format(obj: Union[dict, list]) -> str:
    return json.dumps(obj, ensure_ascii=False)


if __name__ == '__main__':
    text = """Упражнение  130
1. a little. 2. much, little. 3. a few. 4. few. 5. a little,
a few.  6.  a few.  7.  a little,  a little.  8.  few.  9.  a  little.
10.  a  few.  11.  a  little.  12.  a  little.  13.  many,  much.
14. much.  15. much.  16.  a little.  17.  little.  18. little."""
    # print(json_format(ex := parse_exercise(text, parse_exercise_text=True)))
    print(json_format(ex := parse_exercise(text, parse_exercise_text=False)))
    print(len(ex["tasks"]))
