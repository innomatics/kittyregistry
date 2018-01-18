from django.db import models

class Kitty(models.Model):

    kitty_id = models.IntegerField()
    kitty_size = models.ForeignKey('KittySize', default=1, on_delete=models.CASCADE)

    @property
    def image_src(self):
        return 'https://storage.googleapis.com/ck-kitty-image/0x06012c8cf97bead5deae237070f9587f8e7a266d/%s.svg' % self.kitty_id

    @property
    def url(self):
        return 'https://www.cryptokitties.co/kitty/%s' % self.kitty_id

    def __str__(self):
        return 'Kitty %s' % self.kitty_id

class KittySize(models.Model):

    name = models.CharField(max_length=50)
    pixel_size = models.IntegerField()

    def __str__(self):
        return '%s (%s)' % (self.name, self.pixel_size)
