from django.db import models

class Site_Users(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Firstname: {self.firstname} Lastname: {self.lastname} Date: {self.date}"

class Contact(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Username: {self.username} Email: {self.email} Date: {self.date}"

