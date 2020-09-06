from hashlib import md5

prefixes = [i.strip() for i in open("prefixes","r").readlines()]
animals = [i.strip() for i in open("animal_names","r").readlines()]
suffixes = [i.strip() for i in open("suffixes","r").readlines()]
out = open("wordlist","w")
for prefix in prefixes:
	for animal in animals:
		for suffix in suffixes:
			password = prefix+animal+suffix
			if md5(password.encode()).hexdigest() == "58970d579d25f7288599fcd709b3ded3": print(password)



