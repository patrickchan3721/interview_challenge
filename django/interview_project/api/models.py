from django.db import models

class QueryHistory(models.Model):
    domain = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=15)  # Assuming IPv4 addresses are stored as strings
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.domain} - {self.ip_address}"

