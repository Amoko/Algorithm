# coding:utf-8
def get_next(p):
	next=range(len(p))
	next[0]=-1
	i=0
	k=-1
	while i < len(p)-1:
		if k == -1 or p[i] == p[k]:
			i+=1
			k+=1
			next[i]=k
		else:
			k=next[k]
	return next

def kmp(s, p):
	if len(p) == 0:
		return 0

	#get next
	next=get_next(p)

	#start search
	i=0
	j=0
	while i < len(s) and j < len(p):
		if j == -1 or s[i] == p[j]:
			i+=1
			j+=1
		else:
			j=next[j]

	#if matching succeed
	#output the start index in s
	if j == len(p):
		return i-len(p)
	else:	
		return -1

def fun1():
	s = "sababaaa"
	p = "aa"
	answer = kmp(s, p)
	print answer
	#print "Over."

if __name__ == "__main__":
	fun1()
	