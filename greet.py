def greet(name: str) -> str:
    """打招呼：返回「你好，<name>」，并去掉 name 两边的空格。"""
    return "你好，" + name.strip()
