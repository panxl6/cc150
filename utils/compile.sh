#!/bin/bash

declare -A file_name_map
declare -A dir_name_map

# 数组和字符串
file_name_map['1.1']="1.1 判断字符串是否有重复的字符"
file_name_map['1.2']="1.2 反转字符串"
file_name_map['1.3']="1.3 判断两个字符串能否通过重排列变为相同的字符串"
file_name_map['1.4']="1.4 用%20替换掉空格"
file_name_map['1.5']="1.5 字符串压缩"
file_name_map['1.6']="1.6 旋转矩阵"
file_name_map['1.7']="1.7 将矩阵中0元素所在行、列清零"
file_name_map['1.8']="1.8 判断是否为子字符串"
file_name_map['1.9']="1.9 有序数组循环移动，找最小值"


# 链表
file_name_map['2.2']="2.2 取倒数第K的值"


dir_name_map['1']="8.1 数组和字符串"
dir_name_map['2']="8.2 链表"

for key in "${!file_name_map[@]}"; do
	dir_key=`echo "$key" | cut -b 1`
	jupyter nbconvert "jupyter/$key.ipynb" --to markdown --output "../${dir_name_map[$dir_key]}/${file_name_map[$key]}.md"
done
