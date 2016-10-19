#!/usr/bin/python3
# -*- coding:utf-8 -*-
import random

def PermuteWithoutIdentity(A):
	n = len(A)
	for i in range(0,n-1):
		r_A = random.randrange(i+1, n)
		temp = A[i]
		A[i] = A[r_A]
		A[r_A] = temp

arr = [1,2,3,4,5,6,7]
PermuteWithoutIdentity(arr)
print(arr)
