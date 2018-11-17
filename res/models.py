from django.db import models


from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class RssList(models.Model):
	title = models.CharField(max_length=200)
	address=models.CharField(max_length=200)
	categorie = models.ForeignKey(Categorie, null=True, on_delete=models.SET_NULL)
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


# Create your models here.
