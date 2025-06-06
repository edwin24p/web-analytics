from django.db import models


class PageView(models.Model):
    url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)

    def __str__(self):
        """When called as object return url and timestamp as string."""
        return f"{self.url} @ {self.timestamp}"
