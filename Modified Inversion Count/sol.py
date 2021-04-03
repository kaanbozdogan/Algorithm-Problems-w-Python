def mergeSort(arr, n): 
	sorted_arr = [0]*n 
	return mergeSortHelper(arr, sorted_arr, 0, n-1) 


def mergeSortHelper(arr, sorted_arr, left, right): 
	count = 0

	# array has more than one element
	if left < right: 
		mid = (left + right) // 2

		count += mergeSortHelper(arr, sorted_arr, left, mid)
		count += mergeSortHelper(arr, sorted_arr, mid + 1, right) 
		count += merge(arr, sorted_arr, left, mid, right)

	return count 


def merge(arr, sorted_arr, left, mid, right): 
	count = 0
	li = left
	ri = mid + 1
	m = left

	# while both array has elements left
	while li <= mid and ri <= right: 
		# classic sorting happens
		if arr[li] > arr[ri]:
			
			# control if inversion happens
			# we control every index bigger than li until there is an inversion
			i = li
			while arr[i] <= 2 * arr[ri] and i <= mid:
				i += 1
			count += (mid - i + 1) 
			
			sorted_arr[m] = arr[ri]
			ri += 1
			m += 1
		else:
			sorted_arr[m] = arr[li] 
			li += 1
			m += 1

	# copy the rest
	while li <= mid: 
		sorted_arr[m] = arr[li] 
		li += 1
		m += 1
	while ri <= right: 
		sorted_arr[m] = arr[ri] 
		ri += 1
		m += 1

	# sort main array
	for i in range(left, right + 1): 
		arr[i] = sorted_arr[i] 
		
	return count 



arr = [5, 10, 4, 6, 20, 9]  
print(mergeSort(arr, len(arr))) 
