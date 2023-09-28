#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:47:33 2020

@author: yangdongjae
"""


L = []

L.append(5)
L.append(8)
L.append(10)
L.append(15)
L.append(20)
L.append(25)
L.append(30)
L.append(40)
L.append(50)
L.append(54)
L.append(66)
L.append(69)
L.append(83)
L.append(86)
L.append(90)

def find(L, target, start, end):
    if L[(start + end) // 2] < target:
        return find(L,target,(start + end) // 2 +1, end)
    elif L[(start + end) // 2] > target:
        return find(L,target,start,(start + end) // 2 -1)
    else:
        return L[(start + end) // 2]
            #핵심 : 한번 비교를 해서 전체중에 절반을 날려버릴 수 있다. 인덱스 스타트 엔드 컨트롤 할 필요없이 무조건 왼쪽 아니면 오른쪽으로 이동, 만약에 leaf노드까지 갔는데 답이없으면 
            #데이터가 없는것이고, 데이터 추가도 기존의 데이터 구조 건들지않고 서치와 동일한방식으로 따라가다가 leaf노드에 추가.


index = find(L, 67, 0, len(L) - 1)
print(index)