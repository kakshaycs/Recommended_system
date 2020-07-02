from .models import USER, SONG
from random import sample
import random

class Prediction:

	

	def predictUser(self,song_id):
		print("call USER")
		s = SONG.objects.get(pk=song_id+5)
		usr = USER.objects.all();
		Ans = []
		for i in usr:
			a = dict()
			a['user'] = i.id
			a['song'] = song_id
			result = i.A*s.A + i.B*s.B
			result+= i.C*s.C + i.D*s.D  + i.E*s.E
			a['rate'] = round(result)
			if(a['rate']>3.5):
				Ans.append(a)
		print(len(Ans))
		if(len(Ans)>20):
			ANS = sample(Ans,20)
			return ANS
		else:
			return Ans

	def predictSong(self,user_id):
		print("call SONG")
		u = USER.objects.get(pk=user_id+4)
		sng = SONG.objects.all();
		Ans = []
		for i in sng:
			a = dict()
			a['user'] = user_id
			a['song'] = i.id
			result = i.A*u.A + i.B*u.B
			result += i.C*u.C + i.D*u.D + i.E*u.E
			a['rate'] = round( result )
			if(a['rate'] > 3.5):
				Ans.append(a)
		if(len(Ans)>20):
			ANS = sample(Ans,20)
			return ANS
		else:
			return Ans

	def RandomUSERSONG(self):
		sng = sample(list(SONG.objects.all()),20);
		usr = sample(list(USER.objects.all()),20);
		cnt = 0
		Ans = []
		for i in range(20):
			a = dict()
			a['user'] = usr[i].id
			a['song'] = sng[i].id
			result = sng[i].A*usr[i].A + usr[i].B*sng[i].B 
			result += sng[i].C*usr[i].C + sng[i].D*usr[i].D
			result += sng[i].E*usr[i].E
			a['rate'] = round(result)
			Ans.append(a)

		# print(Ans)
		return Ans

	def user(self):
		usr = sample(list(range(10, 97800)),20)
		return usr;

	def song(self):
		sng = sample(list(range(10, 97800)),20)
		return sng;s