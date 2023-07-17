def draw(c):
	mx = max(c, key=lambda q:q[0])[0]
	my = max(c, key=lambda q:q[1])[1]
	
	for y in range(my+1):
		line=""
		for x in range(mx+1):
			if (x,y) in c:
				line+="$"
			else:
				line+=" "
		print(line)
				
coordinates_list = [(1, 2), (3, 4), (5, 6)]
draw(coordinates_list)
