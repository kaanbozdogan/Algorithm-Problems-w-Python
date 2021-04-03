def get_bit(n, i):
	return int((n % pow(10,i+1)) / pow(10,i))


def to_decimal(n):
	dec = 0
	for i in range(0,len(str(n))):  # O(n)
		dec += get_bit(n,i) * pow(2,i)
	return dec


def find_missing(arr):
	for i in range(0,len(arr)-1):  # O(n)
		if get_bit(arr[i],0) == get_bit(arr[i+1],0):
			return to_decimal(arr[i]) + 1

arr = [0,1,10,11,100,110,111,1000]  # 0,1,2,3,4, 6,7,8
print(find_missing(arr))  # prints 5
