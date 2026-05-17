from django.db import models


class MarginCalculation(models.Model):
    aankoopprijs = models.FloatField()
    verkoopprijs = models.FloatField()
    winst = models.FloatField()
    winstmarge = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Margeberekening: {self.winst} winst"