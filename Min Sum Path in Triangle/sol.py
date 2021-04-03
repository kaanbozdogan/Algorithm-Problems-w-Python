def findMinSum(triangle):
	n = len(triangle)
	arr = [[0] * n] * n
	path = [[]] * n

	# init last line of arr and the path
	lastLine = triangle[n-1]
	for i in range(0, len(lastLine)):
		arr[n - 1][i] = lastLine[i]
		path[i] = []

	# row loop
	for i in range(n-2, -1, -1):
		curr = triangle[i]
		# col loop
		for j in range(0, len(curr)):
			sumL = arr[i + 1][j]
			sumR = arr[i + 1][j + 1]
			
			if sumL < sumR:
				minSum = curr[j] + sumL
				minPath = triangle[i+1][j]
			else:
				minSum = curr[j] + sumR
				minPath = triangle[i+1][j+1]
				# if rigth path is samller copy it to the parrent
				for k in range(0,len(path[j])):
					path[j][k] = path[j+1][k]

			arr[i][j] = minSum
			path[j].insert(0,minPath)

	path[0].insert(0,triangle[0][0])
	return path[0]


# main
tri = [[2],
	  [5,4],
	 [1,4,7],
	[8,6,9,6]]

path = findMinSum(tri)
print("path: ", end = "")
for i in range(0,len(path)):
	print(path[i], end = "  ")
print()
