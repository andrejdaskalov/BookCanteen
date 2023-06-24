from django.db import models


# Create your models here.

class BookUser(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rating = models.FloatField(default=0)


    def __str__(self):
        return self.name + " " + self.lastname


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    new = models.BooleanField(default=True)
    
    subjects = [
        ('Math', 'Math'),
        ('Science', 'Science'),
        ('English', 'English'),
        ('History', 'History'),
        ('Art', 'Art'),
        ('Probability and Statistics', 'Probability and Statistics'),
        ('Computer Science', 'Computer Science'),
        ('Economics', 'Economics'),
        ('Business', 'Business'),
        ('Philosophy', 'Philosophy'),
        ('Data Science', 'Data Science'),
        ('Algorithms and Data Structures', 'Algorithms and Data Structures')
    ]

    subject = models.CharField(max_length=100, default="",choices=subjects)
    location = models.CharField(max_length=100, default="")
    condition = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.title + " by: " + self.author
