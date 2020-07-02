class PopulateSong:

	SONG = []
	def getData(self,index):
		return self.SONG[index]

	def __init__(self):
		f = open("SONG.csv", "r")
		f.readline()
		for i in range(127773):
			x = f.readline()
			#print(x.split(','))
			try:
				y = x.split(',')[1]
				z = y.split('[')[1]
				final = z.split(']')[0].split(' ')
				# final.pop()
				Ans=[]
				for i in final:
					if(i != ''):
						Ans.append(float(i))
				self.SONG.append(Ans)
			except:
				print(i)
				print(x)

class PopulateUser:

	USER = []
	def getData(self,index):
		return self.USER[index]

	def __init__(self):
		f = open("USER.csv", "r")
		f.readline()
		for i in range(200002):
			x = f.readline()
			#print(x.split(','))
			try:
				y = x.split(',')[1]
				z = y.split('[')[1]
				final = z.split(']')[0].split(' ')
				# final.pop()
				Ans=[]
				for i in final:
					if(i != ''):
						Ans.append(float(i))
				self.USER.append(Ans)
			except:
				print(i)
				print(x)

	
