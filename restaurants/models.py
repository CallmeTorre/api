from django.db import models

class Restaurant(models.Model):
    id = models.CharField(primary_key = True, editable = True, max_length = 255, verbose_name = u'Id')
    rating = models.IntegerField(verbose_name = u'Rating')
    name = models.CharField(max_length = 255, verbose_name = u'Nombre')
    site = models.CharField(max_length = 255, verbose_name = u'Sitio')
    email = models.CharField(max_length = 255, verbose_name = u'Email')
    phone = models.CharField(max_length = 255, verbose_name = u'Telefono')
    street = models.CharField(max_length = 255, verbose_name = u'Calle')
    city = models.CharField(max_length = 255, verbose_name = u'Ciudad')
    state = models.CharField(max_length = 255, verbose_name = u'Estado')
    lat = models.FloatField(verbose_name = u'Latitud')
    long = models.FloatField(verbose_name = u'Longitud')

    def __unicode__(self):
        return '%s' % (self.name)
    
    class Meta:
        ordering = ('id', 'rating') 