from django.db import models


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    phone_number = models.IntegerField(max_length=12, default=0)
    dob = models.DateField(default="12/05/2000")
    gdpr_consent = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
