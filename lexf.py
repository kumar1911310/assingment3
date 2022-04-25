A = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J" ]
N = 2
def f(length, word):
	if length == N:
		if not any([ word[i-1] == "" and word[i] in A[1:] for i in range(1,N) ]):
			print ("".join(word))
		return
	else:
		for a in A:
			f(length + 1, word + [a])
f(0,[])