picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
]
for row in picture:
	for pixel in row:
		if(pixel==1):
			print('*', end = ' ')
		else:
			print(' ', end = ' ')
	print(' ')

chrismas_tree = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0]
]
insert = '$'
space = ' '
for row in chrismas_tree:
  for pixel in row:
    if(pixel):
      print(insert, end = ' ')
    else:
      print(space, end = ' ')
  print(' ')