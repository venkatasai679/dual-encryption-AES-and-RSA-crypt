from django.db import models
import os
# Create your models here.

class UserModel(models.Model):
    username =  models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = "UserModel"  


class UploadFile(models.Model):
    file = models.FileField(upload_to=os.path.join('static/assets', 'Files'))
    filename = models.CharField(max_length=100)
    uploader = models.EmailField()
    rsa_encrypted_key = models.BinaryField()
    private_key = models.BinaryField()
    encrypted_data = models.BinaryField()
    status = models.CharField(max_length=100, default='Encrypted')

    def __str__(self):
        return self.filename
    
    class Meta:
        db_table = "UploadFile"

        

class UploadFile(models.Model):
    file = models.FileField(upload_to=os.path.join('static/assets', 'Files'))
    filename = models.CharField(max_length=100)
    uploader = models.EmailField()
    rsa_encrypted_key = models.BinaryField()
    private_key = models.BinaryField()
    encrypted_data = models.BinaryField()
    status = models.CharField(max_length=100, default='Encrypted')

    def __str__(self):
        return self.filename
    
    class Meta:
        db_table = "UploadFile"


class RequestFile(models.Model):
    fid = models.IntegerField(null=True)
    requester = models.EmailField()
    file = models.FileField(upload_to=os.path.join('static/assets', 'RequestedFiles'))
    filename = models.CharField(max_length=100)
    uploader = models.EmailField()
    rsa_encrypted_key = models.BinaryField()
    private_key = models.BinaryField()
    encrypted_data = models.BinaryField()
    status = models.CharField(max_length=100, default='Encrypted')
    otp = models.IntegerField(null=True)    

    def __str__(self):
        return self.filename
    
    class Meta:
        db_table = "RequestFile"