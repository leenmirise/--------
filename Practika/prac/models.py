from django.db import models

# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length=30, unique=True)
    userPass = models.CharField(max_length=30)
    userRole = models.IntegerField(default=0)

    # Роли:
    # 1 - преподователь
    # 2 - РОП
    # 3 - админ

    def __str__(self):
        return f"{self.userName},{self.userPass}, {self.userRole}"

    def __repr__(self):
        return f"{self.userName},{self.userPass}, {self.userRole}"