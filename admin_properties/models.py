from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Property(models.Model):
    PROPERTY_TYPES = [
        ('HOUSE', 'Casa'),
        ('APARTMENT', 'Departamento'),
        ('OFFICE', 'Oficina'),
        ('LAND', 'Terreno'),
    ]

    OFFER_TYPE = [
        ('ARRIENDO', 'Arriendo'),
        ('VENTA', 'Venta')
    ]
                    

    address = models.CharField(max_length=255)
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPES)
    offer_type = models.CharField(max_length=8, choices=OFFER_TYPE)
    price = models.DecimalField(max_digits=12, decimal_places=0, validators=[MinValueValidator(0)])
    common_expenses = models.DecimalField(max_digits=8, decimal_places=0, validators=[MinValueValidator(0)], null=True, blank=True)
    square_meters = models.DecimalField(max_digits=8, decimal_places=0, validators=[MinValueValidator(0)])
    bedrooms = models.PositiveSmallIntegerField()
    bathrooms = models.PositiveSmallIntegerField()
    has_parking = models.BooleanField(default=False)
    has_storage_unit = models.BooleanField(default=False)
    floor_number = models.IntegerField(null=True, blank=True)
    amenities = models.TextField(blank=True)
    pets_allowed = models.BooleanField(default=False)
    requirements = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    property_description = models.TextField()
    date_published = models.DateField()


    def __str__(self):
        return f"{self.address} ({self.get_property_type_display()})"
    

    class Meta:
        verbose_name_plural = "Properties"