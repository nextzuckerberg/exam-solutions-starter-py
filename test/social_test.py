

from solutions.social import questiona, tweets

def test_qa():
    result = questiona(tweets)
    assert result == "sandwhoa"


