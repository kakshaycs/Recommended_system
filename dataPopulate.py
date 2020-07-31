class PopulateMovie:

	MOVIE = []
	def getData(self,index):
		return self.MOVIE[index]

	def __init__(self):
		print("constructor call")
		f = open("MOVIE.csv", "r")
		f.readline()
		for j in range(9724):
			x = f.readline()

			try:
				x = x[x.index('[')+1:x.index(']')];
				y = x.split(',')
				# final.pop()
				Ans=[]
				for i in range(len(y)):
					if (i==0):
						Ans.append(int(y[i]))
					else:
						Ans.append(float(y[i]))
				self.MOVIE.append(Ans)
				# print(j,"--",Ans)
			except:
				print(i)
				print(x)

class PopulateUser:

	USER = []
	def getData(self,index):
		return self.USER[index]

	def __init__(self):
		print("constructor call")
		f = open("USER.csv", "r")
		f.readline()
		for j in range(610):
			x = f.readline()
			# print(x.split(','))
			try:
				# print(x.index('['),x.index(']'))
				x = x[x.index('[')+1:x.index(']')];

				# print("x:-",x.split(','))
				y = x.split(',')
				# print("y :- ",y)
				Ans=[]
				for i in range(len(y)):
					if (i==0):
						Ans.append(int(y[i]))
					else:
						Ans.append(float(y[i]))
				self.USER.append(Ans)
				# print(j,"--",Ans)
			except:
				print(i)
				print(x)

	
