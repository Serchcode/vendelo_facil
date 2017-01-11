from django.db import models
from django.conf import settings


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	Telefono = models.CharField(max_length=10,blank=True,null=True)
	Foto = models.ImageField(upload_to="users/%Y/%m/%d",blank=True)


	def __str__(self):
		return 'Perfil del usuario {}'.format(self.user.username)