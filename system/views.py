from django.shortcuts import render
from django.http import HttpResponse
from .models import USER, SONG




def findUSER(song):
	s = SONG.objects.get(pk=song)
	usr = USER.objects.all();
	Ans = []
	for i in usr:
		a = dict()
		a['user'] = i.id
		a['song'] = song
		a['rate'] = round(i.A*s.A + i.B*s.B + i.C*s.C + i.D*s.D + i.E*s.E)
		Ans.append(a)
	return Ans

def findSONG(user):
	u = USER.objects.get(pk=user)
	sng = SONG.objects.all();
	Ans = []
	for i in sng:
		a = dict()
		a['user'] = user
		a['song'] = i.id
		a['rate'] = round(i.A*u.A + i.B*u.B + i.C*u.C + i.D*u.D + i.E*u.E)
		Ans.append(a)
	return Ans

def RandomUSERSONG():
	sng = SONG.objects.all();
	usr = USER.objects.all();
	Ans = []
	for i in usr:
		for j in sng:
			a = dict()
			a['user'] = i.id
			a['song'] = j.id
			a['rate'] = round(i.A*j.A + i.B*j.B + i.C*j.C + i.D*j.D + i.E*j.E)
			Ans.append(a)
	return Ans


def Choose(request):
	print(request.GET)
	context = {}
	target = request.GET.get('id1')
	flag = {
		"value":"Random"
	}
	flag1 = {
		"value":"Unique"
	}
	print(target)
	if(target!=None):
		if(target=="random"):
			print("GET Random data")
			d = RandomUSERSONG()
			context = {
				'Data' : d,
				'flag':flag
			}
		elif(target=='user'):
			ID = request.GET.get('Id');
			d = findSONG(int(ID))
			context = {
				'Data' : d,
				'flag' : flag1
			}
		else:

			ID = request.GET.get('Id');
			d = findUSER(int(ID))
			context = {
				'Data' : d,
				'flag' : flag1
			}
	# data = {
	# 	"user":"akshay",
	# 	"instrument": "Piano",
	# 	"rating":8
	# }
	# context = {
	# 	data : data,
	# }

	return render(request,'system/choose.html',context)

def User(request):
	return render(request,'system/user.html')

def Song(request):
	return render(request,'system/song.html')