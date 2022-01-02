from django.db import models

# Create your models here.


class Author(models.Model):
    class Meta:
        # Display the author objects in ascending order of name
        ordering = ["name"]

        # ordering = ["-name"]  # Descending order

    name = models.CharField(max_length=20)

    def __str__(self):
        # Display the name of the author on admin panel Author list view
        return self.name


class Book(models.Model):
    # We have taken that a book has only one author, but an author can have multiple books
    # Many-to-one relation: Book(Many) -> Author(One)

    # author field of Book has a relation with Author
    # on_delete=models.CASCADE deletes the Book objects of an author if the author is deleted
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    title = models.CharField(max_length=20)
    num_of_pages = models.IntegerField()

    def __str__(self):
        return self.title
