# 项目简介

算法面试圣经(俗称cc150)《Cracking the Coding Interview: 150 Programming Interview Questions and Solutions》。LeetCode上很多的题目都是来自这本书的。

国内有第五版的翻译[《程序员面试金典 第五版》](http://download.csdn.net/download/ab920322/9029587)。目前已经更新到了第六版。

由于题量由150题增加到189道题([第六版](http://download.csdn.net/download/u011433684/9553267)应该叫cc189了吧)，而且官方给出的是Java版，这整理了第六版的Python实现。


# 使用指南
```bash
# 安装jupyter
pip3 install jupyter

# 进入项目下的jupter目录,启动jupyter服务器.访问地址http://localhost:8888/tree
jupyter notebook
```

# 题目列表
| 序号           | 题目           | 备注  |
| ------------- |----------------| -----|
| 1.1    | [1.1 判断字符串是否有重复的字符](https://github.com/panxl6/cc150/blob/master/8.1%20数组和字符串/1.1%20判断字符串是否有重复的字符.md) |  |
| 1.2    | [1.2 反转字符串](https://github.com/panxl6/cc150/blob/master/8.1%20数组和字符串/1.2%20反转字符串.md) |  |
| 1.3    | [1.3 判断两个字符串能否通过重排列变为相同的字符串](https://github.com/panxl6/cc150/blob/master/8.1%20数组和字符串/1.3%20判断两个字符串能否通过重排列变为相同的字符串.md) |  |
| 1.4    | [1.4 用%20替换掉空格](https://github.com/panxl6/cc150/blob/master/8.1%20数组和字符串/1.4%20用%2520替换掉空格.md) |  |
| 1.5    | [1.5 字符串压缩](https://github.com/panxl6/cc150/blob/master/8.1%20数组和字符串/1.5%20字符串压缩.md) |  |
| 1.6    | [1.6 旋转矩阵](https://github.com/panxl6/cc150/blob/master/8.1%20数组和字符串/1.6%20翻转矩阵.md) |  |
| 1.7    | [1.7 将矩阵中0元素所在行、列清零](https://github.com/panxl6/cc150/blob/master/8.1%20数组和字符串/1.7%20将矩阵中0元素所在行、列清零.md) |  |
| 1.8    | [1.8 判断是否为子字符串](https://github.com/panxl6/cc150/blob/master/8.1%20数组和字符串/1.8%20判断是否为子字符串.md) |  |
| 1.9    | [1.9 有序数组循环移动，找最小值](https://github.com/panxl6/cc150/blob/master/8.1%20数组和字符串/1.9%20有序数组循环移动，找最小值.md) |  |
| 2.1    | [2.1 移除未排序链表中的重复节点](https://github.com/panxl6/cc150/blob/master/8.2%20链表/2.1%20移除未排序链表中的重复节点.md) |  |
| 2.2    | [2.2 取倒数第K的值](https://github.com/panxl6/cc150/blob/master/8.2%20链表/2.2%20取倒数第K的值.md) |  |
| 2.4    | [2.4 按基准值将链表分为两部分](https://github.com/panxl6/cc150/blob/master/8.2%20链表/2.4%20按基准值将链表分为两部分.md) |  |



# 备注
- 链表节点的定义。
```python
# Definition for singly-linked list.
class ListNode:
    
    def __init__(self, x):
        self.val = x
        self.next = None
```
- 相关的公共放在了`jupyter/common`目录，引入方式如下：
```python
import os
import sys
sys.path.insert(0, os.path.abspath('./common'))
```


# 计划表

- [ ] 统一代码格式
- [ ] 美化文字格式，提升阅读体验
- [ ] 增加LeetCode的相关专题
- [ ] 完成后续的章节
- [ ] 增加示意图或动画
- [ ] 增加第六版的内容
- [ ] 对比官方的Java版答案，校验一次
- [ ] 抽象测试用例运行框架，实现一个Online judge