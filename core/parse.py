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
    text = """
Упражнение  148

1. Where is Nick?  — He is at the lecture.  2. Father 
goes  to  work  every  day.  3.  Yesterday  father  was  at 
work and  mother was at home.  4.  Yesterday I went  to 
the  library,  I  borrowed  a very  interesting book  at  the 
library. 5. Kate was sitting at the table. There were books 
and exercise books on the table.  Her father went up to 
the table and put a vase on the table. He put some flowers 
into the vase.  6. We went to the exhibition yesterday. 
We saw a lot of paintings at the exhibition.  7.  Where 
is Tom? — He is at the stadium. He always goes to the 
stadium on Sunday. And his sister goes to the swimming 
pool. She is at the swimming pool now. 8. Do you like 
going to the theatre?  9.  When we came to the railway 
station, we put our things on the platform and sat down 
on a bench.  Mother went to the shop and bought some 
lemonade.  10. At the lesson yesterday the teacher said 
to me,  “There are  two  mistakes  on the blackboard.  Go 
to the blackboard and correct the mistakes!”  11.  Were 
you  at  the  concert  yesterday?  —  No,  we  worked  at 
the  library  and  then  we  went  to  the  park.  We  played 
in the park and then we sat on the grass.  12. There are 
not so many children in the yard today.  13.  There are 
so many students at the lecture today.

"""
    # print(json_format(ex := parse_exercise(text, parse_exercise_text=True)))
    print(json_format(ex := parse_exercise(text, parse_exercise_text=False)))
    print(len(ex["tasks"]))
