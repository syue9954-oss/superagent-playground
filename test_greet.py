from greet import greet


def test_greet_chinese():
    assert greet("小明") == "你好，小明"


def test_greet_empty():
    assert greet("") == "你好，"


def test_greet_strips_space():
    assert greet("  小红  ") == "你好，小红"
