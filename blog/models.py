from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=225)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')




#Add the blog app to the settings

#Create a migration

#Migrate

#Add to the admin
