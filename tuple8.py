t=tuple(eval(input()))
p=()
for i  in t:
	if i not in p:
		if t.count(i) > 1:
			p+=(i,)



print(p)
