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
    text = """Упражнение 161
Вставьте предлоги, где необходимо.
1. We tried to speak _ him, but he did not want
to listen _ us. He did not even look _ us and did not
answer _ our questions. 2. Your brother complains
_ you. He says you always laugh _ him, never speak
_ him and never answer _ his questions. 3. When
I entered _ the room, everybody looked _ me with
surprise: they had not expected _ mo. 4. At the end _
the street she turned _ the corner, walked _ the bus
stop and began waiting _ the bus. 5. My mother is
afraid _ rats. 6. “What do you complain _?” asked
the doctor. 7. Don't enter _ the room. 8. What are
you laughing _ ? 9. They did not want to listen _
me. 10. Wait _ me. I'll be back _ a few minutes.
11. Yesterday the teacher spoke _ us about the
architecture _ St Petersburg. 12. My grandmother
often complains _ headache. 13. I am sorry, I cannot speak _ you now, the professor is waiting _ me.
I must go _ the institute and explain _ him some
details _ our work. Come _ the evening, I shall listen
_ you very attentively and answer _ all your questions. 14. Turn _ the corner _ the house and look _
the flowers grown _ my mother: aren't they beautiful? 15. He was an excellent pupil, and the teachers never complained _ him. 16. She complained _
feeling bad and could not answer _ the questions _
the teacher. 17. _ nine o'clock the lecturer entered
_ the hall, walked up _ the table, put his bag _ it,
looked _ everybody and began his lecture. The lecture, as all the lectures _ this professor, was very
interesting, and the students listened _ him with
great attention."""
    print(json_format(ex := parse_exercise(text, parse_exercise_text=True)))
    # print(json_format(ex := parse_exercise(text, parse_exercise_text=False)))
    print(len(ex["tasks"]))
