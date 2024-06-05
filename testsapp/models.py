from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class UserIdent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, verbose_name=_('full name'))
    personal_number = models.CharField(max_length=50, verbose_name=_('peronal number'))
    birth_date = models.DateField(verbose_name="birth date")

    def __str__(self):
        return self.user.username


class TestOrigin(models.Model):
    name = models.CharField(max_length=264, verbose_name=' ტესტის წარმომავლობა', blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = ' Test Origion'
        verbose_name_plural = ' Test Origion'


class TestType(models.Model):
    test_type_name = models.CharField(max_length=264, verbose_name=' ტესტის ტიპი', blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.test_type_name

    class Meta:
        verbose_name = ' Test Type'
        verbose_name_plural = ' Test Type'


class Test(models.Model):
    test_origin = models.ForeignKey(TestOrigin, on_delete=models.CASCADE, verbose_name=' ტესტის წარმომავლობა',
                                    blank=True, null=True, default=None)
    number = models.IntegerField(verbose_name=' ნომერი', blank=True, null=True, default=None)
    test_type = models.ForeignKey(TestType, on_delete=models.CASCADE, verbose_name=' ტესტის ტიპი',
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

