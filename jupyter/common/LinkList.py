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

    def get_list_length(self, head):
        if head is None:
            return 0
        
        count = 0
        while head is not None:
            count += 1
            head = head.next
        return count

    def to_array(self, head):
        if head is None:
            return []
        
        array = []
        while head is not None:
            array.append(head.val)
            head = head.next
        return array

    def get_node_by_value(self, head, value):
        if head is None:
            return head
        
        while head is not None:
            if head.val == value:
                return head
            head = head.next
        
        return None

    # 将链表B相交于链表A的位置joinPosition
    def join_list(self, A, B, joinPosition):
        if A is None or B is None:
            return

        while True:
            if B.next is None:
                break
            B = B.next
        
        count = 1
        while A is not None:
            if count == joinPosition:
                B.next = A
                break
            count += 1
            A = A.next

    def make_list_cycle(self, A, cyclePosition):
        if A is None:
            return

        tempA = A
        while tempA.next is not None:
            tempA = tempA.next
        
        count = 1
        while A is not None:
            if count == cyclePosition:
                tempA.next = A
                break
            count += 1
            A = A.next



