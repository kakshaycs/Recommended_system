from .models import USER, MOVIE
from random import sample
import random

class Prediction:
	def predictUser(self,mid):
		print("call USER",mid)
		s = MOVIE.objects.get(movieid=mid)
		usr = USER.objects.all();
		Ans = []
		for i in usr:
			a = dict()
			a['user'] = i.userid
			a['movie'] = mid
			result = i.A*s.A + i.B*s.B
			result+= i.C*s.C + i.D*s.D  + i.E*s.E
			a['rate'] = round(result)
			if(a['rate']>3.5):
				if(a['rate']<=5):
					Ans.append(a)
		print(len(Ans))
		if(len(Ans)>20):
			ANS = sample(Ans,20)
			return ANS
		else:
			return Ans

	def predictMovie(self,uid):
		print("call SONG")
		u = USER.objects.get(userid=uid)
		mov = MOVIE.objects.all();
		Ans = []
		for i in mov:
			a = dict()
			a['user'] = uid
			a['movie'] = i.movieid
			result = i.A*u.A + i.B*u.B
			result += i.C*u.C + i.D*u.D + i.E*u.E
			a['rate'] = round( result )
			if(a['rate'] > 3.5):
				if(a['rate']<=5):
					Ans.append(a)
		if(len(Ans)>20):
			ANS = sample(Ans,20)
			return ANS
		else:
			return Ans

	def RandomUSERMOVIE(self):
		mov = sample(list(MOVIE.objects.all()),20);
		usr = sample(list(USER.objects.all()),20);
		cnt = 0
		Ans = []
		for i in range(min(len(mov),len(usr))):
			a = dict()
			a['user'] = usr[i].userid
			a['movie'] = mov[i].movieid
			result = mov[i].A*usr[i].A + usr[i].B*mov[i].B 
			result += mov[i].C*usr[i].C + mov[i].D*usr[i].D
			result += mov[i].E*usr[i].E
			a['rate'] = round(result);
			if(round(result) > 5):
				a['rate'] = 5;
			Ans.append(a)

		return Ans

	def user(self):
		usr = sample(list(USER.objects.all()),20);
		ans = []
		for i in usr:
			ans.append(i.userid);
		return ans;

	def movie(self):
		mov = sample(list(MOVIE.objects.all()),20);
		ans = []
		for i in mov:
			ans.append(i.movieid);
		return ans;