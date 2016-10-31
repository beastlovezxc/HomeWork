#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Bean
import math
A = (math.sqrt(5)-1)/2.0

def Hash(k,m):
	x = (A*k-int(A*k))*m
	return int(x)

keys = [61,62,63,64,65]
m = 1000

for k in keys:
	print('Hash[%d] = %d' % (k,Hash(k,m)))
