from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    first_name = models.CharField(max_length=128, null=False, blank=True)
    middele_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=False, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    language = models.CharField(max_length=128, null=False, blank=True)
    is_translator = models.BooleanField(default=False, null=False, blank=True)


class Publication(BaseModel):
    name = models.CharField(max_length=128, null=False, blank=False)
    phone_number = PhoneNumberField(null=True, blank=True)
    address = models.CharField(max_length=128, null=False, blank=False)


class Book(BaseModel):
    title = models.CharField(max_length=128, null=False, blank=False)
    year = models.IntegerField(
        null=False,
        default=2020,
        validators=[MaxValueValidator(4000), MinValueValidator(500)],
    )
    translator = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="book_translator"
    )
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="book_author"
    )
    page_numbers = models.PositiveIntegerField(null=False)
    description = models.TextField(null=True, blank=True)
    isbn = models.IntegerField(null=False, blank=True)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
