import random


qicksort_swap_count = 0
insertion_sort_swap_count=0


def quicksort(arr):
	quicksort_helper(arr,0,len(arr)-1)	


def quicksort_helper(arr,first,last):
	if first<last:
		pivot = partition(arr,first,last)
		quicksort_helper(arr,first,pivot-1)
		quicksort_helper(arr,pivot+1,last)


def partition(arr,first,last):
	global qicksort_swap_count

	pivotVal = arr[first]
	up = first
	down = last
	
	while True:
		while up<last and pivotVal>=arr[up]:
			up+=1
		
		while pivotVal<arr[down]:
			down-=1
	
		if up<down:
			swap(arr, up, down);
			qicksort_swap_count+=1
		
		if up>=down:
			break

	swap(arr, first, down);
	return down;


def swap(arr,i,j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp




def insertion_sort(arr):
	for nextPos in range(1,len(arr)):
		insert(arr, nextPos)

def insert(arr,nextPos):
	global insertion_sort_swap_count
	nextVal = arr[nextPos]

	while nextPos>0 and nextVal<arr[nextPos-1]:
		arr[nextPos] = arr[nextPos-1]
		nextPos-=1
		insertion_sort_swap_count+=1

	arr[nextPos] = nextVal



# mian function to test swap counts
arr1 = []
arr2 = []

print("initializing array with 1000 elements\n")

for x in range(1,1000):
	rand = random.randint(0,1000)
	arr1.append(rand)
	arr2.append(rand)


quicksort(arr1)
print("Swaps in quick sort: \t ", qicksort_swap_count)

insertion_sort(arr2)
print("Swaps in insertion sort: ", insertion_sort_swap_count)
