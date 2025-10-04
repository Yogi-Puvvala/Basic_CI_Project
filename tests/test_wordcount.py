from src.wordcount import count_words

def test_count_words():
    assert count_words("Hello world") == 2
    assert count_words("") == 0
    assert count_words("One two three") == 3
