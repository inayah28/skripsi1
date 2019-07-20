from django.db import models

# Create your models here.
class Matkul(models.Model):
	kdmk = models.CharField(max_length=9)
	matkul = models.CharField(max_length=50)
	sks = models.CharField(max_length=1, blank="true")
	semester = models.CharField(max_length=1, blank="true")
	def __str__(self):
		return "{}.{}".format(self.id,self.kdmk)

class Profesi(models.Model):
	kdprofesi = models.CharField(max_length=9)
	profesi = models.CharField(max_length=50)
	def __str__(self):
		return "{}.{}".format(self.id,self.kdprofesi)

class Matkur(models.Model):
	kdmkr = models.CharField(max_length=9)
	matkur = models.CharField(max_length=50)
	semester = models.CharField(max_length=1)
	def __str__(self):
		return "{}.{}".format(self.id,self.kdmkr)

class Profesi_Matkul(models.Model):
	kdprofesi = models.CharField(max_length=9,blank="true")
	kdmk = models.CharField(max_length=9)
	matkul = models.CharField(max_length=50)
	sks = models.CharField(max_length=1, blank="true")
	semester = models.CharField(max_length=1, blank="true")
	def __str__(self):
		return "{}.{}".format(self.id,self.kdmk)

class Profesi_Matkur(models.Model):
	kdprofesi = models.CharField(max_length=9,blank="true")
	kdmkr = models.CharField(max_length=9)
	matkur = models.CharField(max_length=50)
	semester = models.CharField(max_length=1, blank="true")
	def __str__(self):
		return "{}.{}".format(self.id,self.kdmkr)

	
	
