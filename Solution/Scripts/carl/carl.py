from hashlib import md5

gods = [i.strip() for i in open("gods.txt","r").readlines()]
states = [i.strip() for i in open("states.txt","r").readlines()]

for god in gods:
	for state in states:
		password = god+state
		if md5(password.encode()).hexdigest() == '661ded81b6b99758643f19517a468331': print(password)

