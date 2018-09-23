from django.db import models

# Create your models here.


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=100)
    member_age = models.IntegerField()
    member_address = models.CharField(max_length=250)
    contact_number = models.CharField(max_length=12)
    join_date = models.DateField(default='')
    member_photo = models.FileField()
    member_bio = models.CharField(max_length=500)

    # class Meta:
    #     # to manage from db client
    #     # managed = False

    def __unicode__(self):
        return self.member_name + ' | ' + self.member_address


class Dependent(models.Model):
    GENDER_CHOICE = (('M', 'MALE'), ('F', 'FEMALE'), ('T', 'TRANS'))

    id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    dependent_name = models.CharField(max_length=100)
    dependent_age = models.IntegerField()
    dependent_gender = models.CharField(max_length=6, choices=GENDER_CHOICE, default='')

    def __unicode__(self):
        return self.dependent_name
