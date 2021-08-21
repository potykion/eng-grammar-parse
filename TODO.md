# Задачки

## Exercises

- [ ] 3_pronouns.txt
  - [x] Причесать: каждое предложение на одной строке
  - [ ] Троеточие - ужасно, надо заменить на _ / заместо ... сделать инпут, а остальной текст - спан
  - [ ] Сейв прогресса (ввода)
  

## Keys

- [ ] 3_pronouns.txt
  - стрип точки
  - сплит по ,
    

# Предобработка

## Полезные реплейсы

- " .1" > ". I"

# Парс 

## Для задачек

```python
# core/parse.py
text = """..."""
print(json_format(ex := parse_exercise(text)))
print(len(ex["tasks"]))
```

## Для ответов

```python
# core/parse.py
text = """..."""
print(json_format(ex := parse_exercise(text, parse_exercise_text=False)))
print(len(ex["tasks"]))
```

https://app.quicktype.io/