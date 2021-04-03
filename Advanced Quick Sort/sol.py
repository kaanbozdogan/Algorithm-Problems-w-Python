# quicksort is more efficent with larger arrays but insertion sort is more efficent when it comes to smaller arrays because of lesser comparasions and swaps.
# using insertion sort when array gets smaller enhances the performance of the sorting.
def enhanced_quick_sort(arr, treshold):  # Treshold: the element count which sorting alg. uses insertion s. for the rest of the sorting
	quick_sort_helper(arr, 0, len(arr)-1, treshold)


def quick_sort_helper(arr, start, end, treshold):		
	if start < end:	
		if (end - start) > treshold + 1:  # if more elements will be sorted than the treshold, classic quick sort used
			pivot = partition(arr, start, end)
			quick_sort_helper(arr, start, pivot-1, treshold)
			quick_sort_helper(arr, pivot+1, end, treshold)
		else:
			inseriton_sort(arr, start, end);


def inseriton_sort(arr, p, r):  # generic insertion sort func
	for j in range(p+1, r+1):
		i = j - 1
		key = arr[j]
	
		while (i > (p - 1)) and (arr[i] > key):
			arr[i+1] = arr[i]
			i -= 1

		arr[i+1] = key


def partition(arr, p, r):  # generic partition func
	x = arr[r]
	i = p - 1
	
	for j in range(p, r):
		if arr[j] <= x:
			i += 1
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp

	temp = arr[r]
	arr[r] = arr[i+1]
	arr[i+1] = temp
	
	return i + 1


arr = [5,2,15,7,10,3,18,9,16,19,4,20,14,11,13,1,6,12,8,17]
print("Array UNsorted: ", arr)
enhanced_quick_sort(arr,4)
print("Array sorted: ", arr)
