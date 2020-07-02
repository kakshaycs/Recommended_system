from django.shortcuts import render
from django.http import HttpResponse
from .models import USER, SONG
from random import sample
from .Prediction import Prediction





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
	p = Prediction();

	if(target!=None):
		if(target=="random"):
			print("GET Random data")
			d = p.RandomUSERSONG()
			context = {
				'Data' : d,
				'flag':flag
			}
		elif(target=='user'):
			ID = request.GET.get('Id');
			d = p.predictSong(int(ID))
			
			context = {
				'Data' : d,
				'flag' : flag1
			}
		else:

			ID = request.GET.get('Id');
			d = p.predictUser(int(ID))
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
	p = Prediction();
	return render(request,'system/user.html',{'data':p.user()})

def Song(request):
	p = Prediction();
	return render(request,'system/song.html',{'data':p.song()})