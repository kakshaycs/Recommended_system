# f = open("SONG.csv", "r")

# def getProcessData(x):
# 	x = f.readline()
# 	y = x.split(',')[1]
# 	z = y.split('[')[1]
# 	final = z.split(']')[0].split(' ')
# 	final.pop()
# 	Ans=[]
# 	for i in final:
# 		if(i != ''):
# 			Ans.append(float(i))
# 	return Ans;

# print(getProcessData(f.readline()))

# from system.models import SONG, USER
# from dataPopulate import PopulateSong,PopulateUser

# for i in range(69999,80000):
# ...     Ar = U.getData(i)
# ...     u = USER(A=Ar[0],B=Ar[1],C=Ar[2],D=Ar[3],E=Ar[4])
# ...     u.save()


from dataPopulate import PopulateSong,PopulateUser

p = PopulateUser();
print(p.getData(10))