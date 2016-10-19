#!/usr/bin/python3
# -*- coding:utf-8 -*-

import random

def PermuteWithAll(A):
	for i in range(0, len(A)):
		r_A = random.randrange(0, len(A))
		temp = A[i]
		A[i] = A[r_A]
		A[r_A] = temp

arr = [1,2,3,4,5,6,7]
PermuteWithAll(arr)
print(arr)