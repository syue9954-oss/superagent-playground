# superagent-playground

dsh-superagent 的练习场：一个最小的 Python 项目，用来观察「有人派活 → 智能体干活 → 交付 PR」的完整流程。

## 现在的状态

`greet.py` 里的 `greet()` **故意没实现**，所以测试会失败：

```
$ pytest
FAILED test_greet.py::test_greet_chinese      - NotImplementedError
FAILED test_greet.py::test_greet_empty        - NotImplementedError
FAILED test_greet.py::test_greet_strips_space - NotImplementedError
3 failed
```

## 任务是什么

实现 `greet(name)`，让它：

1. 返回 `你好，<name>`
2. `name` 为空时返回 `你好，`
3. 把 `name` 两边的空格去掉（`"  小红  "` → `你好，小红`）

## 怎么跑

```bash
pip install pytest
pytest -q
```

三条全绿就说明做对了。

## 怎么让智能体来做

在 Issue 里 @ 智能体的账号，它会改 `greet.py`、提交一个 PR，你审核后合并。
