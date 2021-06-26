from django.db import models

# Create your models here.

class CarPlan(models.Model):
    paln_name = models.CharField(max_length=50)
    year_of_warrenty = models.PositiveIntegerField(default=1)
    finance_plan = models.CharField(max_length=50, default='Unavailable')

    def __str__(self):
        return self.paln_name

class CarSpaces(models.Model):
    car_plan = models.ForeignKey(CarPlan, on_delete=models.SET_NULL, null=True)
    car_brand = models.CharField(max_length=80)
    car_model = models.CharField(max_length=100)
    production_year = models.CharField(max_length=40)
    car_body = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=50)

    def __str__(self):
        return self.car_brand
