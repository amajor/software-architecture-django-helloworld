from django.db import models


class Name(models.Model):
    first_name_text = models.CharField(max_length=50)
    last_name_text = models.CharField(max_length=50)

    def __str__(self):
        return ' '.join((self.first_name_text, self.last_name_text))

    def full_name(self):
        return ' '.join((self.first_name_text, self.last_name_text))

    def first_name(self):
        return self.first_name_text

    def last_name(self):
        return self.last_name_text
