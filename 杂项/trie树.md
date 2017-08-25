
# Trie树的简单实现
1. 构建trie树
2. 查找是否在trie树中。

TODO:
自动补全功能


```python
# coding=utf-8


class Trie:

    def __init__(self):

        # 入口节点
        self.__root = {}

    def build(self, temp_str):

        if temp_str is None or len(temp_str) == 0:
            return

        temp_list = list(temp_str)

        node = self.__root

        for item in temp_list:
            if item not in node:
                node[item] = {}
            node = node[item]

    def search(self, temp_str):

        if temp_str is None or len(temp_str) == 0:
            return

        temp_list = list(temp_str)

        node = self.__root

        for item in temp_list:
            if item in node:
                node = node[item]
            else:
                return False
        return True


trie = Trie()
trie.build('abcd')
trie.build('abd')
print(trie.search('abe'))

```
