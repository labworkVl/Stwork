from django.db import models


class Streets(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.name,)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'streets'


class Doma(models.Model):
    street = models.ForeignKey(Streets, on_delete=models.SET_NULL, null=True)
    nomer = models.IntegerField()
    bukva = models.CharField(max_length=10)

    def __str__(self):
        return '%s %s%s' % (self.street, self.nomer, self.bukva)

    class Meta:
        ordering = ['nomer', 'bukva']
        verbose_name_plural = 'doma'


class Kws(models.Model):
    dom = models.ForeignKey(Doma, on_delete=models.SET_NULL, null=True)
    nomer = models.IntegerField()
    bukva = models.CharField(max_length=10)

    def __str__(self):
        return '%s %s%s' % (self.dom, self.nomer, self.bukva)

    class Meta:
        ordering = ['nomer', 'bukva']
        verbose_name_plural = 'kws'


class Ls(models.Model):
    kw = models.ForeignKey(Kws, on_delete=models.SET_NULL, null=True)
    nomer = models.IntegerField()
    fio = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s %s' % (self.kw, self.nomer, self.fio)

    class Meta:
        ordering = ['nomer', 'fio']
        verbose_name_plural = 'lss'


class Adresa(models.Model):
    adr_type = ((0, 'street'), (1, 'dom'), (2, 'kw'), (3, 'ls'), )
    type = models.IntegerField(choices=adr_type)



