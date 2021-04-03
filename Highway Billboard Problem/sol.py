def maxIncome(x, r, distance, mileRest):
	# maximum money earned at each index of the road
	earned = [0] * (distance + 1)
	# x's of ads used to reach max money earned for each index of the road
	ads = [[]] * (distance + 1)
	# init every index with different list
	for i in range(0, distance + 1):
		ads[i] = []
	# advertisement index
	xi = 0
	# minimum distance we can put adds with
	minDist = mileRest + 1
	if x[0] == 0:
		earned[0] = r[0]

	# control every index of road
	for i in range(1,distance+1):
		# control if there is any ads left
		if xi < len(x):
			# if an ad exists that we can put to that index of the road
			if x[xi] == i:
				# if we can put another ad before, with putting an ad to this index
				if i >= minDist:
					# take the one which brings more income:
					# 1- putting an ad to this index with putting ads to previous possible indexes
					# 2- keeping the ad at previous index of the road and not putting another to this one
					if earned[i - minDist] + r[xi] > earned[i - 1]:
						maxEarn = earned[i - minDist] + r[xi]
						ads[i].extend(ads[i - minDist])
						ads[i].append(x[xi])
					else:
						maxEarn = earned[i - 1]
						ads[i].extend(ads[i-1])
				# we can only chhose one ad
				else:
					# take the one which brings more income:
					# 1- put this ad to this index and remove the previous one
					# 2- keep the previous one
					if r[xi] > earned[i - 1]:
						maxEarn = r[xi]
						ads[i].append(x[xi])
					else:
						maxEarn = earned[i - 1]	
						ads[i] = ads[i-1]

				earned[i] = maxEarn
				# get to the next index of the road
				xi += 1

			# if there aren't any ads we can put to that index of the road
			else:
				# copy the previous
				earned[i] = earned[i - 1]
				ads[i].extend(ads[i-1])
			
		# if no ads left we can put to the road
		else:
			# copy the prev index
			earned[i] = earned[i - 1]
			ads[i] = ads[i - 1]
		

	# printing the results	
	print("Total money earned:", earned[distance])
	print("Ads used at distances ", end = "")
	for i in range(0,len(ads[distance])):
		print(ads[distance][i], end = ", ")
	print()



x = [3, 5, 8, 9, 15, 19, 25, 29]
r = [4, 2, 3, 5, 7, 6, 1, 6]
M = 30
dist = 4
maxIncome(x, r, M, dist)
