from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel


class User(AbstractUser):
    pass


class SiteConfigurations(SingletonModel):
    standard_board = models.ForeignKey('Board', models.SET_NULL, verbose_name=_('Standard Board'), null=True)

    def __str__(self):
        return self._meta.verbose_name.title()

    class Meta:
        verbose_name = _("Site Configuration")


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
        OTHER = 'O', _("Other")

    name = models.CharField(_('Name'), max_length=64)
    student_number = models.PositiveIntegerField(_('Student number'))
    state = models.CharField(max_length=2, choices=State.choices, default=State.SUBMITTED)
    type = models.CharField(_('Data structure'), max_length=1, choices=Type.choices, default=Type.HASH)
    staff = models.BooleanField(_('Staff'), default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    submission = models.FileField(_('Submission'), upload_to='submissions')
    ip = models.GenericIPAddressField(verbose_name='IP-address', protocol='IPv4')
    board = models.ForeignKey('Board', null=True, on_delete=models.SET_NULL, related_name="submissions")

    time_load = models.FloatField(null=True)
    time_check = models.FloatField(null=True)
    time_size = models.FloatField(null=True)
    time_unload = models.FloatField(null=True)
    time = models.FloatField(null=True)

    def __str__(self):
        return f"{self.name} - {self.date_created}"


class Dictionary(models.Model):
    name = models.CharField(_("Name"), max_length=16, unique=True)
    file = models.FileField(_('File'), upload_to='dictionaries')

    class Meta:
        verbose_name = _("Dictionary")
        verbose_name_plural = _("Dictionaries")

    def __str__(self):
        return self.name


class Text(models.Model):
    name = models.CharField(_("Name"), max_length=16, unique=True)
    file = models.FileField(_("File"), upload_to='texts')

    def __str__(self):
        return self.name


class TestCase(models.Model):
    text = models.ForeignKey(Text, on_delete=models.CASCADE)
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['text', 'dictionary']

    def __str__(self):
        return f"{self.text} with {self.dictionary}"


class Board(models.Model):
    title = models.CharField(_("Title"), max_length=64)
    slug = models.SlugField(_('Slug'), unique=True)
    testcases = models.ManyToManyField(TestCase, related_name='used_in')

    def __str__(self):
        return self.title
