num = 5342

newNum = num
numLen = len(str(num))

print('Num ', 'Max ', 'Min ', 'Subs')

# Limit to 8 iterations
for x in range(0, 8):

	numStr = str(newNum)
	longNum, shortNum = '', ''

	subsNum = 0

	# Store individual numbers in array + sort
	numArr = []
	for i in numStr:
		numArr.append(str(i))
	numArr.sort()

	# Find largest number
	for l in reversed(range(numLen)):
		longNum += numArr[l]

	# Find smallest number
	for l in range(0, numLen):
		shortNum += numArr[l]

	# Substract numbers
	subsNum = str(int(longNum) - int(shortNum))

	# If new result is less than 4 digits, add zeros
	if len(subsNum) < numLen:
		for p in range(len(subsNum), numLen):
			subsNum = '0' + subsNum

	# Print and save in variable
	print(numStr, longNum, shortNum, subsNum)
	newNum = subsNum

	if newNum == '6174':
		break