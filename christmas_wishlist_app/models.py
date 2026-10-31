from django.db import models


class FamilyMember(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.name}"

class Gift(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    link = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.family_member}"
