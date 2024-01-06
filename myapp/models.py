from django.db import models
import uuid
from django.contrib.auth.models import User


def generate_uuid():
    x=1
    pkey=uuid.uuid4().hex
    pkey+=str(x)
    x+=1
    return pkey

def user():
    return User.objects.first()

class base(models.Model):
    reference_id=models.CharField(max_length=50,unique=True,primary_key=True,default=generate_uuid)
    is_delete=models.BooleanField(default=False)
    created_by=models.ForeignKey(User,default=user,db_column='created_by',on_delete=models.PROTECT,related_name='+')
    created_at=models.DateTimeField()
    updated_by=models.ForeignKey(User,db_column="updated_by",on_delete=models.PROTECT,null=True)
    updated_at=models.DateTimeField(null=True)
    
    class Meta:
        abstract=True
        

class Form(base):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.CharField(max_length=100)
    city=models.CharField(max_length=75)
    
    class Meta:
        db_table='form'
        
    def __str__(self):
        return self.username
