import random
import sys
sys.setrecursionlimit(100000)

def youWin(table):
	print("\t", end="")
	for i in range(len(table)): print(i+1, end=" ")
	print("")
	print("")
	for x in range(len(table)):
		print(x+1, end="\t")
		for y in range(len(table)):	
			if(table[x][y] == 9):
				print("*", end=" ")
			else:
				if(table[x][y] == 0):
					print('.', end= " ")
				else:
					print(table[x][y], end = " ")

		print('\t', x+1, end="\n")
	print("you Win. Have a good time ;)")

def checkWinOrLose(table, showTable):
	win1 = True
	win2 = True
	lose = False
	for i in range(len(table)):
		for j in range(len(table)):
			if(table[i][j] == 9 and showTable[i][j] == 3):
				lose = True
			if(table[i][j] != 9 and showTable[i][j] != 1):
				win1 = False
			if(table[i][j] == 9 and showTable[i][j] != 2):
				win2 = False
	if(lose):
		return('lose')
	elif(win1 or win2):
		return('win')
	else:
		return('none')

def showCell(table, showTable, x, y):
	if(x>len(table)-1 or x<0 or y > len(table)-1 or y<0):
		return
	showTable[x][y] = 1
	if(table[x][y] == 0 and x<=len(table)-2 and y<=len(table)-2):
		if(table[x-1][y]!= 9 and showTable[x-1][y] == 0):
			showCell(table, showTable, x-1, y)
		if(table[x+1][y]!= 9 and showTable[x+1][y] == 0):
			showCell(table, showTable, x+1, y)
		if(table[x][y-1]!= 9 and showTable[x][y-1] == 0):
			showCell(table, showTable, x, y-1)
		if(table[x][y+1]!= 9 and showTable[x][y+1] == 0):
			showCell(table, showTable, x, y+1)
	else:
		return
	
def youLose(table):
	print("\t", end="")
	for i in range(len(table)): print(i+1, end=" ")
	print("")
	print("")
	for x in range(len(table)):
		print(x+1, end="\t")
		for y in range(len(table)):	
			if(table[x][y] == 9):
				print("*", end=" ")
			else:
				if(table[x][y] == 0):
					print('.', end= " ")
				else:
					print(table[x][y], end = " ")

		print('\t', x+1, end="\n")
	print("you lose. Good luck next time ;)")

def help():
	print("Enter the row number and column number with one space between them:")
	print("2 3 c")
	print("2 3 f")
	print("2 3 u")
	print( "\"c\" for check the cell, \"f\" for flag it and \"u\" for unflag the cell ")

def invalidInput():
	print("Input is not Valid; Try again")

def getInpnCheck(table, showTable, numOfMines, numOfFlags):
	print("Input the row and column of the cell that you want to select(H for help):")
	inputLine = list(input().split(' '))
	if(inputLine[0] == 'H'):
		help()
		return(numOfFlags)
	else:
		x = int(inputLine[0])
		y = int(inputLine[1])
		if(x<1 or x>len(table) or y<1 or y>len(table)):
			invalidInput()
			return(numOfFlags)
		else:
			if(table[x-1][y-1] == 9 and inputLine[2] == 'c'):
				showTable[x-1][y-1] = 3
				return(numOfFlags)
			elif(inputLine[2] == 'f'):
				if(int(numOfFlags) >= numOfMines):
					print("You can't Flag the cells anymore")
					return(numOfFlags)
				else:
					showTable[x-1][y-1] = 2
					numOfFlags = numOfFlags + 1
					return(numOfFlags)
			elif(inputLine[2] == 'u'):
					if(showTable[x-1][y-1] != 2):
						print("This cell is not Flagged yet")
						return(numOfFlags)
					else:
						showTable[x-1][y-1] = 0
						numOfFlags = numOfFlags - 1
						return(numOfFlags)
			else:
				showCell(table, showTable, x-1, y-1)
				return(numOfFlags)


def generateMines(table, n):
	for i in range(n):
		x = random.randint(0, n-1)
		y = random.randint(0, n-1)
		if(table[x][y] == 9):
			i = i-1
			continue
		table[x][y] = 9

def checkTop(table, i, j, n):
	if(i!= 0):
		if(table[i-1][j]!= 9):
			table[i-1][j] = table[i-1][j] + 1
		if(j!= 0):
			if(table[i-1][j-1]!= 9):
				table[i-1][j-1] = table[i-1][j-1] + 1
		if(j!= n-1):
			if(table[i-1][j+1]!= 9):
				table[i-1][j+1] = table[i-1][j+1] + 1

def checkBot(table, i, j, n):
	if(i!= n-1):
		if(table[i+1][j]!= 9):
			table[i+1][j] = table[i+1][j] + 1
		if(j!= 0):
			if(table[i+1][j-1]!= 9):
				table[i+1][j-1] = table[i+1][j-1] + 1
		if(j!= n-1):
			if(table[i+1][j+1]!= 9):
				table[i+1][j+1] = table[i+1][j+1] + 1

def checkLeft(table, i, j, n):
	if(j!= 0):
		if(table[i][j-1]!= 9):
			table[i][j-1] = table[i][j-1] + 1
		
def checkRight(table, i, j, n):
	if(j!= n-1):
		if(table[i][j+1]!= 9):
			table[i][j+1] = table[i][j+1] + 1
		


def generateTableNums(table, n):
	for i in range(n):
		for j in range(n):
			if(table[i][j] == 9):
				checkTop(table, i, j, n)
				checkBot(table, i, j, n)
				checkLeft(table, i, j, n)
				checkRight(table, i, j, n)

def printTable(table, showTable):
	print("\t", end="")
	for i in range(len(table)): print(i+1, end=" ")
	print("")
	print("")
	for x in range(len(table)):
		print(x+1, end="\t")
		for y in range(len(table)):
			if(showTable[x][y] == 0):
				print("X", end=" ")
			else:
				if(showTable[x][y] == 2):
					print('F', end= " ")
				elif(table[x][y] == 0):
					print('.', end= " ")
				else:
					print(table[x][y], end = " ")

		print('\t', x+1, end="\n")
		

print("Size: ", end="")
size = int(input())
print("# of Mines: ", end="")
numOfMines = int(input())
numOfFlags = 0
table = [[0 for x in range(size)] for x in range(size)]
showTable = [[0 for x in range(size)] for x in range(size)]

generateMines(table, numOfMines)
generateTableNums(table, size)

while True :
	printTable(table, showTable)
	numOfFlags = getInpnCheck(table, showTable, numOfMines, numOfFlags)
	state = checkWinOrLose(table, showTable)
	if(state == 'lose'):
		youLose(table)
		break
	elif(state == 'win'):
		youWin(table)
		break
	else:
		continue
	
	


