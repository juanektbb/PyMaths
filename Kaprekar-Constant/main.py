num = 9999

newNum = num

numLen = len(str(num))


for x in range(0, 8):

	numStr = str(newNum)
	longNum, shortNum = '', ''

	subsNum = 0

	numArr = []
	for i in numStr:
		numArr.append(str(i))

	numArr.sort()

	for l in reversed(range(numLen)):
		longNum += numArr[l]

	for l in range(0, numLen):
		shortNum += numArr[l]

	subsNum = str(int(longNum) - int(shortNum))

	if len(subsNum) < numLen:
		for c in range(len(subsNum) - numLen):
			subsNum += '0'

	print(newNum, longNum, shortNum, subsNum)
	newNum = subsNum

	if newNum == '6174':
		break


