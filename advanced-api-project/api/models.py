from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# api/models.py
class Author(models.Model):
    # Author's name, can be linked to multiple books
    name = models.CharField(max_length=255)

class Book(models.Model):
    # Book's title
    title = models.CharField(max_length=255)
    # Year of publication, with validation in the serializer
    publication_year = models.IntegerField()
    # ForeignKey establishing the relationship between Author and Book
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

