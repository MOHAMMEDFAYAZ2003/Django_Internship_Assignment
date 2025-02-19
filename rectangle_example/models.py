from django.db import models

class Rectangle(models.Model):
    width = models.IntegerField()
    height = models.IntegerField(default=10)  # Ensure this field exists

    def __str__(self):
        return f"Rectangle {self.width}x{self.height}"
