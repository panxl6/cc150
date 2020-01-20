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


# 第六版题目

| 序号           | 题目           |
| ------------- |----------------|
| 1.1    | **判定字符是否唯一** 实现一个算法,确定一个字符串的所有字符是否全都不同。假使不允许使用额外的数据结构,又该如何处理? |
| 1.2    | **判定是否互为字符重排** 给定两个字符串,请编写程序,确定其中一个字符串的字符重
新排列后,能否变成另一个字符串。 |
| 1.3    | **URL 化** 编写一种方法,将字符串中的空格全部替换为 %20 。假定该字符串尾部有足够的空间存放新增字符,并且知道字符串的“真实”长度。(注:用 Java 实现的话,请使用字符数组实现,以便直接在数组上操作。) <br>*示例*:<br>*输入:* "Mr John Smith", 13 <br>*输出:* "Mr%20John%20Smith" |
| 1.4    | **回文排列** 给定一个字符串,编写一个函数判定其是否为某个回文串的排列之一。回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。回文串不一定是字典当中的单词。<br>*示例:*<br>*输入:* Tact Coa<br>*输出:* True (排列有 "taco cat" 、 "atco cta" ,等等) |
| 1.5    | **一次编辑** 字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。给定两个字符串,编写一个函数判定它们是否只需要一次(或者零次)编辑。<br>*示例:* <br> pale, ple -> true <br>pales, pale -> true <br>pale, bale -> true <br> pale, bake -> false |
| 1.6    | **字符串压缩** 利用字符重复出现的次数,编写一种方法,实现基本的字符串压缩功能。比如,字符串 aabcccccaaa 会变为 a2b1c5a3 。若“压缩”后的字符串没有变短,则返回原先的字符串。你可以假设字符串中只包含大小写英文字母(a 至 z) |
| 1.7    | **旋转矩阵** 给定一幅由 N × N 矩阵表示的图像,其中每个像素的大小为 4 字节,编写一种方法,将图像旋转 90 度。不占用额外内存空间能否做到? |
| 1.8    | **零矩阵** 编写一种算法,若 M × N 矩阵中某个元素为 0,则将其所在的行与列清零。 |
| 1.9    | **字符串轮转** 假定有一种 isSubstring 方法,可检查一个单词是否为其他字符串的子串。给定两个字符串 s1 和 s2 ,请编写代码检查 s2 是否为 s1 旋转而成,要求只能调用一次isSubstring (比如, waterbottle 是 erbottlewat 旋转后的字符串)。 |



# 计划表

- [ ] 统一代码格式
- [ ] 美化文字格式，提升阅读体验
- [ ] 增加LeetCode的相关专题
- [ ] 完成后续的章节
- [ ] 增加示意图或动画
- [ ] 增加第六版的内容
- [ ] 对比官方的Java版答案，校验一次
- [ ] 抽象测试用例运行框架，实现一个Online judge