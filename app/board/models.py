from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    pass


class Submission(models.Model):
    class State(models.TextChoices):
        SUBMITTED = 'SU', "Submitted"
        RUNNING = 'RU', 'Running'
        ACCEPTED = 'AC', 'Accepted'
        REJECTED = 'RE', 'Rejected'
        DELETED = 'DE', 'Deleted'

    class Type(models.TextChoices):
        TRIE = 'T', _("Trie")
        HASH = 'H', _("Hashtable")

    name = models.CharField(_('Name'), max_length=64)
    student_number = models.PositiveIntegerField(_('Student number'))
    state = models.CharField(max_length=2, choices=State.choices, default=State.SUBMITTED)
    type = models.CharField(_('Data structure'), max_length=1, choices=Type.choices)
    staff = models.BooleanField(_('Staff'), default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    submission = models.FileField(_('Submission'), upload_to='static/uploads')
    ip = models.GenericIPAddressField(verbose_name='IP-address', protocol='IPv4')

    time_load = models.FloatField(null=True)
    time_check = models.FloatField(null=True)
    time_size = models.FloatField(null=True)
    time_unload = models.FloatField(null=True)
    time = models.FloatField(null=True)

    def __str__(self):
        return f"{self.name} - {self.date_created}"
