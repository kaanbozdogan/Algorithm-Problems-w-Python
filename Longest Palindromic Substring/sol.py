def longestPalSubstr(str) :
	n = len(str)
 
	# if table[i][j] == true -> str(i:j) is a palindrome
	table = [[0 for i in range(n)] for j in range(n)]
	 
	# substrings with size 1 are palindrome
	for i in range(0,n):
		table[i][i] = True
	palLength = 1

	# init table for 2 element subsets
	palStart = 0
	for i in range(0,n-1):
		if str[i] == str[i + 1]:
			table[i][i+1] = True
			palStart = i
			palLength = 2
	 
	# check subsets with 3 and more elemens
	for l in range(3,n):
		# check all starting indexes
		for s in range(0,n-l+1):
			# init end of the controlled substring
			e = s + l - 1
			# if the starting and the ending characters are equal
			# and the substring between them is palindromic
			# substring between indexes s and e is palindromic
			if str[s] == str[e] and table[s + 1][e - 1]:
				table[s][e] = True
				# update the new palindrome substring
				if l > palLength:
					palStart = s
					palLength = l

	# longest palindrome subset
	return str[palStart: palStart + palLength]
 
str = "asptenetor"
result = longestPalSubstr(str)
print("Longest Substring:", result)
