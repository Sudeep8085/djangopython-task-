from django.db import models

# Create your models here.
class Patient(models.Model):
    f_name= models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)

    gen=(
        ('1',"male"),
        ('2',"female"),
        ('3',"other")
    )

    gender= models.CharField(max_length=3,choices=gen)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    address= models.CharField(max_length=45)

    visitDate = models.DateField()

    def __str__(self):
        return self.f_name


