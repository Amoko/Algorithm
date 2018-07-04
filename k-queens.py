"""
Created on Wed Jul  4 20:53:06 2018

@author: Yonji
"""
import numpy as np
import time
import inspect

def showchess(loc):
	if inspect.stack()[1][3] == "recursion_k":
		chessboard = np.zeros((m,n))
	else:
		chessboard = np.zeros((n,n))
	
	for e in loc:
		chessboard[e[0]][e[1]] = 1
	print(chessboard)
	print()

# check conflict
def isok(loc, pos):
	flag = True
	for e in loc:
		if abs(e[0]-pos[0]) == abs(e[1]-pos[1]):
			flag = False
			break
		if e[1]==pos[1]:
			flag = False
			break
	return flag



#--------------------------------------
#             n queens
#--------------------------------------

# add element in next row
def recursion_n(loc, row):
	if row == n:
		showchess(loc)
		global count
		count += 1
		return None
	for column in range(n):
		pos = [row, column]
		if isok(loc, pos):
			loc_new = loc + [pos]
			recursion_n(loc_new, row+1)
	return None

# init the 1st row element
def nqueens():
	global count
	count = 0
	loc = []
	row = 0
	for column in range(n):
		pos = [row, column]
		loc_new = loc + [pos]
		recursion_n(loc_new, row+1)
	print(count)

#--------------------------------------
#             k queens
#--------------------------------------
# add element in next row
def recursion_k(loc, r):
	if len(loc) == k:
		showchess(loc)
		global count
		count += 1
		return None
	for row in range(r,m-(k-len(loc))+1):
		for column in range(n):
			pos = [row, column]
			if isok(loc, pos):
				loc_new = loc + [pos]
				recursion_k(loc_new, row+1)
	return None

# init the 1st row element
def kqueens():
	global count
	count = 0
	loc = []
	r = 0
	for row in range(r,m-(k-len(loc))+1):
		for column in range(n):
			pos = [row, column]
			loc_new = loc + [pos]
			recursion_k(loc_new, row+1)
	print(count)
if __name__ == "__main__":
	print("Start.",time.ctime())
	
	m, n, k = 6, 6, 4
	kqueens()
	
	n = 8
	nqueens()

	print("End.",time.ctime())