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


def parse_exercise(exercise_text: str) -> dict:
    text = exercise_text.strip().split("\n", 2)
    return {
        'exercise_number': int(re.search(r"Упражнение (\d+)", text[0]).group(1)),
        'exercise_text': text[1],
        'tasks': parse_tasks_text(text[2])
    }


def json_format(obj: Union[dict, list]) -> str:
    return json.dumps(obj, ensure_ascii=False)


if __name__ == '__main__':
    text = """Упражнение 121
Вставьте одно из следующих слов: some, any, по, the, а или оставьте пропуски незаполненными.

1. I'm afraid there's ... juice in ... fridge. Would
you like ... lemonade? 2. My friends from Chicago
can't speak ... foreign languages. 3. She bought ...
new books yesterday. 4. Where are ... books which
you borrowed from ... library yesterday? 5. Did you
buy ... apples when you were at ... shop? 6. We could
not skate because there was ... snow on ... ice. 7. ...
house must; have ... windows. 8. Most people like
... music. 9. There was ... meat on Nick's plate and ...
fish on Tom's. 10. We saw ... houses in the distance.
11. ... cats like ... milk. 12. They stopped in ... front
of ... house where Tom lived. 13.1 showed him ... way
to ... station. 14. What is ... name of ... street on
which you live? 15. I want to say ... words to your
sister. 16. ... tea in this glass is cold. 17. ... sun was
high in ... sky. 18. Oh, there are ... apples in ... fruit
bowl: ... children have eaten all of them. Please put
... apples into ... fruit bowl. 19. Yesterday we had ...
fish for dinner. 20. He gave me ... coffee. 21. I drank
... cup of ... coffee after ... dinner. 22. What ... success! 23. We didn't have ... problems in using this
printer with ... computer. 24. Nowadays, watching
... TV is ... complete waste of ... time.
"""
    print(json_format(ex := parse_exercise(text)))
    print(len(ex["tasks"]))
