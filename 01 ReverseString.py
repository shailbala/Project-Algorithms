def reverseWord(s):
    t = ""
    for i in range(len(s)-1, -1, -1):
        t = t + s[i]
    return t

# Driver code
if __name__ == "__main__":
	t = int(input())
	while(t>0):
		s=input()
		print(reverseWord(s))
		t = t-1
