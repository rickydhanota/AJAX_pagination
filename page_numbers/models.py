from django.db import models

class Lead(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    from_date=models.DateTimeField()
    to_date=models.DateTimeField()
    email=models.EmailField(max_length=254)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)