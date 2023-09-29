from django.db import models

# Create your models here.
GEN_CH=(
    ('male','MALE'),
    ('female','FEMALE'),
)

class stud_info(models.Model):
    stud_id = models.AutoField(primary_key=True)
    stud_fname = models.CharField(max_length=55, blank=True, null=True)
    stud_lname = models.CharField(max_length=55, blank=True, null=True)
    stud_class = models.CharField(max_length=10, blank=True, null=True)
    stud_email = models.EmailField()
    stud_age = models.IntegerField()
    stud_address = models.TextField()
    stud_city = models.CharField(max_length=99)
    stud_contact = models.CharField(max_length=10, blank=True, null=True)
    stud_bloodgroup=models.CharField(max_length=10)
    stud_DOB=models.DateField()
    stud_gen=models.CharField(max_length=6,choices=GEN_CH)


    # renames the instances of the models
    # with the id name
    def __int__(self):
        return self.stud_id

