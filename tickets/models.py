from django.db import models

class Ticket(models.Model):
    PRIORITY_CHOICES = [
        ("Төмен", "Төмен"),
        ("Орташа", "Орташа"),
        ("Жоғары", "Жоғары"),
    ]
    title = models.CharField("Тақырып", max_length=200)
    description = models.TextField("Сипаттама")
    priority = models.CharField("Басымдық", max_length=20, choices=PRIORITY_CHOICES, default="Орташа")
    status = models.CharField("Мәртебе", max_length=20, default="Жаңа")

    def __str__(self):
        return self.title
