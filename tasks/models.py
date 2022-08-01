from telnetlib import STATUS
from django.db import models
from django.contrib.auth import get_user_model

class task(models.Model):
    # Criando banco
    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    upadate_at = models.DateTimeField(auto_now=True)
    # Mostrando nome na área admin
    def __str__(self):
        return self.title

# makemigrations: fazer ou construir a migração
# migrate: fazer ela
# createsuperuser: criar ADM