def knapsack(W, wt, val):
	table = [0] * (W + 1)
	
	arr = [[]] * (W + 1) #2d list
	for i in range(0,W+1):
		arr[i] = [0] * len(wt)


	for i in range(0,W + 1):
		for j in range(0,len(wt)):
			if wt[j] <= i:
				# calculate the total value of the new subset
				newWeigth = table[i - wt[j]] + val[j]
				# if it is more valuable than the previous subset then update it
				if table[i] < newWeigth:
					# update the most value we can get with i capacity
					table[i] = newWeigth
					# copy the item counts of previously found subset
					for k in range(0,3)	:
						arr[i][k] = arr[i-wt[j]][k]
					# increment count of the item with j weigth in the subset
					arr[i][j] += 1

	return arr[W];

wt = [5,4,2]
val = [10,4,3]
subset = knapsack(9, wt, val)

for i in range(0,len(wt)):
	print("weigth:", wt[i], ", value:", val[i],", count:", subset[i])
  
