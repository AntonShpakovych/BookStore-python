from django.db import models


class Category(models.Model):
    name = models.CharField(max_length = 30, null= False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Author(models.Model):
    first_name = models.CharField(max_length = 30, null = False)
    last_name = models.CharField(max_length = 30, null = False)

    def __str__(self):
        return self.first_name

class Book(models.Model):
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length = 30, null= False)
    description = models.TextField(max_length = 1000, null= False)
    quantity = models.PositiveSmallIntegerField(null = False)
    price = models.DecimalField(max_digits = 10, decimal_places = 2, null= False)
    width = models.DecimalField(max_digits = 4, decimal_places = 2, null = False)
    length = models.DecimalField(max_digits = 4, decimal_places = 2, null = False)
    height = models.DecimalField(max_digits = 4, decimal_places = 2, null = False)
    materials = models.CharField(max_length = 30, null = False)
    year_of_publication = models.PositiveSmallIntegerField(null = False)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    category = models.ForeignKey('Category', on_delete = models.CASCADE)
   
    
    def all_authors(self):
       return ', '.join([author.first_name +' ' + author.last_name for author in list(self.authors.all())])

    def __str__(self):
        return self.title
