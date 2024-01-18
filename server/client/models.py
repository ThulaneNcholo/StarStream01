from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name
    

class CelebritiesModel(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    categories = models.ManyToManyField(
        CategoryModel, blank=True, default=None, related_name='celeb_categories')
    category =  models.ForeignKey(CategoryModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='category')
    price = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name
    
class SignUpsModel(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name
