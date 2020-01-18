#!/bin/python3
# coding=utf-8

# Definition for singly-linked list.
class ListNode:
    
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList:
    
    # 根据列表创建单链表
    def get_list(self, data):
        if len(data) == 0:
            return None
        
        temp = head = ListNode(data[0])
        for i in range(1, len(data)):
            temp.next = ListNode(data[i])
            temp = temp.next
        
        return head
    
    # 逐个输出链表的内容
    def print_list(self, head):
        if head is None:
            return
        
        while head is not None:
            print(head.val)
            head = head.next

    def to_array(self, head):
        if head is None:
            return []
        
        array = []
        while head is not None:
            array.append(head.val)
            head = head.next
        return array

