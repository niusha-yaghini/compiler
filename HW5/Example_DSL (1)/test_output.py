bombs = [[0 for y in range(80)] for x in range(5)]
bombs[0][1] = -1
bombs[3][5] = -1
bombs[4][7] = -1
hint = True
if(hint):
	for row in range(len(bombs)):
		for column in range(len(bombs[0])):
			if(bombs[row][column]==-1 and hint):
				for x in range(row-1, row+2):
					for y in range(column-1, column+2):
						if(0<=x<len(bombs) and 0<=y<len(bombs[0])):
							if(bombs[x][y]!=-1):
								bombs[x][y]+=1
for i in bombs:
	for j in i:
		if(j == -1):
			print('*', end='')
		elif (j == 0):
			print('#', end='')
		else:
			print(j, end='')
	print()
