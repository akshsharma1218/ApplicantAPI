from django.db import models

class Applicant(models.Model):
    Gen = [
        ('Prefer not to respond','Prefer not to respond'),
        ('Male','Male'),
        ('Female','Female')
    ]
    Status = [
        ('Pending','Pending'),
        ('Selected','Selected'),
        ('Rejected','Rejected')
    ]
    f_name = models.CharField(max_length=30)
    m_name = models.CharField(max_length=50,null=True)
    l_name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(choices = Gen, max_length = 21)
    status = models.CharField(choices = Status, max_length = 8)
    resume = models.FileField(upload_to='resume', blank=True)
