from django.db import models

class UserRank(models.Model):
	user_name = models.TextField(max_length = 40)
	user_point = models.IntegerField(default=0)
	def __str__(self):
		return "name :"+self.user_name+" point :"+str(self.user_point)