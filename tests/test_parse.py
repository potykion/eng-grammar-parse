from core.parse import parse_tasks_text, parse_exercise


def test_parse_tasks_text():
    text = """1. There аге ... buses today and I can't go shopping. 2. There is ... caviare in the can. I love it.
Would you like ... ? 3. Please don't offer her ...
chips. She doesn't want ... . 4. Can I have ... milk
in my tea? I don't like it black. 5. There is ... ink
in my pen. 6. Is there ... snow in the street this
morning? 7. My mother likes ... music. 8. Are there
... chess players here? 9. There are ... diagrams in
the new book. 10. Are there ... newspapers on the
table? 11. Was there ... water in the glass or ... milk?
12. There was ... soap in the soap dish; he used it to
wash his hands. 13. There was ... soap in the box:
it smells of ... soap. 14. There is ... tea for you on
the table. 15. Do you like ... apples? 16. Were there
... of our boys at the stadium? 17.. There were ...
students of our group at the Opera House yesterday. 18. Will there be ... concerts at the club next
month? 19. There were ... yellow and green pencils on
the table. 20. People need ... oxygen for breathing.
21. Are there ... mistakes in my dictation? — Yes,
there are ... . 22. My brother doesn't like ... onions."""

    assert parse_tasks_text(text) == [
        "There аге ... buses today and I can't go shopping.",
        "There is ... caviare in the can. I love it. Would you like ... ?",
        "Please don't offer her ... chips. She doesn't want ... .",
        "Can I have ... milk in my tea? I don't like it black.",
        "There is ... ink in my pen.",
        "Is there ... snow in the street this morning?",
        "My mother likes ... music.",
        "Are there ... chess players here?",
        "There are ... diagrams in the new book.",
        "Are there ... newspapers on the table?",
        "Was there ... water in the glass or ... milk?",
        "There was ... soap in the soap dish; he used it to wash his hands.",
        "There was ... soap in the box: it smells of ... soap.",
        "There is ... tea for you on the table.",
        "Do you like ... apples?",
        "Were there ... of our boys at the stadium?",
        ". There were ... students of our group at the Opera House yesterday.",
        "Will there be ... concerts at the club next month?",
        "There were ... yellow and green pencils on the table.",
        "People need ... oxygen for breathing.",
        "Are there ... mistakes in my dictation? — Yes, there are ... .",
        "My brother doesn't like ... onions.",
    ]


def test_parse_exercise():
    exercise_text = """
    Упражнение 115
Вставьте some, any, no, every или их производные.
1. To know ... is to know ... . 2. ... is rotten in the
state of Denmark (W. Shakespeare). 3. Wealth is ...
without health. 4. ... is good in its season. 5. Can
I have ... milk? — Yes, you can have ... . 6. Will you
have ... tea? 7. Give me ... books, please. I have ...
to read at home. 8. Put ... sugar in her tea: she does





not like sweet tea. 9. Is ... the matter with you? Has
... offended you? I see by your face that ... has happened. 10. We did not see ... in the hall. 11.... was
present at the lesson yesterday. 12. He is busy. He
has ... time to go to the cinema with us. 13. Do you
need ... books,to prepare your report?» 14. Have you ...
questions? Ask me ... you like, I shall try to answer
... question. 15. ... liked that play: it was very dull.
16. If ... is ready, we shall begin our experiment.
17. Money isn't ... in the world. 18. She's got ... in
common with her brother. 19. Don't believe ... she
says. 20. We enjoyed ... minute of the concert last
Sunday."""
    assert parse_exercise(exercise_text) == {
        "exercise_number": 115,
        "exercise_text": "Вставьте some, any, no, every или их производные.",
        "tasks": ["To know ... is to know ... .", "... is rotten in the state of Denmark (W. Shakespeare).",
                  "Wealth is ... without health.", "... is good in its season.",
                  "Can I have ... milk? — Yes, you can have ... .", "Will you have ... tea?",
                  "Give me ... books, please. I have ... to read at home.",
                  "Put ... sugar in her tea: she does not like sweet tea.",
                  "Is ... the matter with you? Has ... offended you? I see by your face that ... has happened.",
                  "We did not see ... in the hall.", "... was present at the lesson yesterday.",
                  "He is busy. He has ... time to go to the cinema with us.",
                  "Do you need ... books,to prepare your report?»",
                  "Have you ... questions? Ask me ... you like, I shall try to answer ... question.",
                  "... liked that play: it was very dull.", "If ... is ready, we shall begin our experiment.",
                  "Money isn't ... in the world.", "She's got ... in common with her brother.",
                  "Don't believe ... she says.", "We enjoyed ... minute of the concert last Sunday."]
    }
