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
        "There аге _ buses today and I can't go shopping.",
        "There is _ caviare in the can. I love it. Would you like _ ?",
        "Please don't offer her _ chips. She doesn't want _ .",
        "Can I have _ milk in my tea? I don't like it black.",
        "There is _ ink in my pen.",
        "Is there _ snow in the street this morning?",
        "My mother likes _ music.",
        "Are there _ chess players here?",
        "There are _ diagrams in the new book.",
        "Are there _ newspapers on the table?",
        "Was there _ water in the glass or _ milk?",
        "There was _ soap in the soap dish; he used it to wash his hands.",
        "There was _ soap in the box: it smells of _ soap.",
        "There is _ tea for you on the table.",
        "Do you like _ apples?",
        "Were there _ of our boys at the stadium?",
        "There were _ students of our group at the Opera House yesterday.",
        "Will there be _ concerts at the club next month?",
        "There were _ yellow and green pencils on the table.",
        "People need _ oxygen for breathing.",
        "Are there _ mistakes in my dictation? — Yes, there are _ .",
        "My brother doesn't like _ onions.",
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
        "exerciseNumber": 115,
        "exerciseText": "Вставьте some, any, no, every или их производные.",
        "tasks": ["To know _ is to know _ .", "_ is rotten in the state of Denmark (W. Shakespeare).",
                  "Wealth is _ without health.", "_ is good in its season.",
                  "Can I have _ milk? — Yes, you can have _ .", "Will you have _ tea?",
                  "Give me _ books, please. I have _ to read at home.",
                  "Put _ sugar in her tea: she does not like sweet tea.",
                  "Is _ the matter with you? Has _ offended you? I see by your face that _ has happened.",
                  "We did not see _ in the hall.", "_ was present at the lesson yesterday.",
                  "He is busy. He has _ time to go to the cinema with us.",
                  "Do you need _ books,to prepare your report?»",
                  "Have you _ questions? Ask me _ you like, I shall try to answer _ question.",
                  "_ liked that play: it was very dull.", "If _ is ready, we shall begin our experiment.",
                  "Money isn't _ in the world.", "She's got _ in common with her brother.",
                  "Don't believe _ she says.", "We enjoyed _ minute of the concert last Sunday."]
    }
