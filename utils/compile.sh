#!/bin/bash

declare -A file_name_map
declare -A dir_name_map

# 数组和字符串
file_name_map['1.1']="1.1 判断字符串是否有重复的字符"
file_name_map['1.2']="1.2 判定是否互为字符重排"
file_name_map['1.3']="1.3 URL化"
file_name_map['1.4']="1.4 用%20替换掉空格"
file_name_map['1.5']="1.5 字符串压缩"
file_name_map['1.6']="1.6 旋转矩阵"
file_name_map['1.7']="1.7 将矩阵中0元素所在行、列清零"
file_name_map['1.8']="1.8 判断是否为子字符串"
file_name_map['1.9']="1.9 有序数组循环移动，找最小值"


# 链表
file_name_map['2.1']="2.1 移除未排序链表中的重复节点"
file_name_map['2.2']="2.2 取倒数第K的值"
file_name_map['2.4']="2.4 按基准值将链表分为两部分"


## 目录映射
result_dir="markdown"

for key in "${!file_name_map[@]}"; do
	dir_key=`echo "$key" | cut -b 1`
	jupyter nbconvert "jupyter/$key.ipynb" --to markdown --output "../$result_dir/${file_name_map[$key]}.md"
done
