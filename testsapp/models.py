from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class UserIdent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, verbose_name=_('full name'))
    personal_number = models.CharField(max_length=50, verbose_name=_('peronal number'))
    birth_date = models.DateField(verbose_name="birth date")
    points = models.IntegerField(blank=True, null=True, default=None)
    coins = models.IntegerField(blank=True, null=True, default=None)

    def __str__(self):
        return self.user.username


class Category1(models.Model):
    name = models.CharField(max_length=264, verbose_name=' Category3', blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = ' Category1'
        verbose_name_plural = ' Category1'


class Category2(models.Model):
    name = models.CharField(max_length=264, verbose_name=' Category3', blank=True, null=True, default=None)
    category1 = models.ForeignKey(Category1, on_delete=models.CASCADE, verbose_name=' ტესტის კატეგორია1',
                                    blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    testImage = models.ImageField(upload_to='photos/Category3_photos/%y/%m/%d/', verbose_name=' ფოტო',
                                  blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = ' Category2'
        verbose_name_plural = ' Category2'


class Category3(models.Model):
    name = models.CharField(max_length=264, verbose_name=' Category3', blank=True, null=True, default=None)
    category2 = models.ForeignKey(Category2, on_delete=models.CASCADE, verbose_name=' ტესტის კატეგორია',
                                    blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    testImage = models.ImageField(upload_to='photos/Category3_photos/%y/%m/%d/', verbose_name=' ფოტო',
                                  blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.name} (Category2: {self.category2.name}, " \
               f"Category1: {self.category2.category1.name})"

    class Meta:
        verbose_name = ' Category3'
        verbose_name_plural = ' Category3'


class Test(models.Model):
    test_origin = models.ForeignKey(Category3, on_delete=models.CASCADE, verbose_name=' ტესტის კატეგორია',
                                    blank=True, null=True, default=None)
    testText = models.TextField(verbose_name=' ტესტის შინაარსი', blank=True, null=True, default=None)

    testDescription = models.TextField(max_length=5264, verbose_name=' აღწერა',
                                       blank=True, null=True, default=None)
    testImage = models.ImageField(upload_to='photos/test_photos/%y/%m/%d/', verbose_name=' ფოტო',
                                  blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.testText

    class Meta:
        verbose_name = ' Tests'
        verbose_name_plural = ' Tests'


class Answers(models.Model):
    tests = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name=' ტესტის ტიპი',
                              blank=True, null=True, default=None)
    answer_text = models.TextField(verbose_name=' პასუხის შინაარსი', blank=True, null=True, default=None)
    answers_image = models.ImageField(upload_to='photos/Answer_photos/%y/%m/%d/', verbose_name=' ფოტო', blank=True,
                      default=None, null=True)
    is_correct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.answer_text

    class Meta:
        verbose_name = ' answers'
        verbose_name_plural = ' answers'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('product name'))
    price = models.IntegerField(blank=True, null=True, default=None)
    productImage = models.ImageField(upload_to='photos/product_photos/%y/%m/%d/', verbose_name=' პროდუქტის ფოტო',
                                  blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


