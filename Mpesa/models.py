from django.db import models
from django.core.validators import MinValueValidator

class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class MpesaResponseBody(AbstractBaseModel):
    body = models.JSONField()


class Transaction(AbstractBaseModel):
    phonenumber = models.CharField(max_length=100)
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    receipt_no = models.CharField(max_length=100)

    def __str__(self):
        return self.receipt_no
    

