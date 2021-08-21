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

    sentences = [s.strip() for s in sentences]
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
        'exercise_number': int(re.search(r"Упражнение\s+(\d+)", text[0]).group(1)),
        'tasks': parse_tasks_text(text[-1])
    }
    if parse_exercise_text:
        res['exercise_text'] = text[1]

    return res


def json_format(obj: Union[dict, list]) -> str:
    return json.dumps(obj, ensure_ascii=False)


if __name__ == '__main__':
    text = """Упражнение  121
1. no, the, some. 2. any. 3. some. 4. the, the. 5. any,
the. 6. -, the. 7. a, -. 8. -. 9. some, some.  10. some.
11. -, -.
12.  -,  the.  13.  the,  the.  14.  the,  the.

15. some.  16. the.  17. the, the.  18.  no, the, the, some,
the.  19. -.  20. some. 21. a, -,  -.   22. a. 23. any, any.
24. -, a, -."""
    print(json_format(ex := parse_exercise(text, parse_exercise_text=False)))
    print(len(ex["tasks"]))
