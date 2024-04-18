from django.db import models

class weatherdata(models.Model):
    city = models.CharField(max_length = 100)
    country_code = models.CharField(max_length = 10)
    coord = models.CharField(max_length = 30)
    temp = models.CharField(max_length = 30)
    pressure = models.CharField(max_length = 30)
    humidity = models.CharField(max_length = 30)
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Weather in {self.city}, {self.country_code}"