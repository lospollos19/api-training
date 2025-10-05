from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_PROFESSOR = "PROFESSOR"
    ROLE_ADMIN = "ADMIN"

    ROLE_CHOICES = (
        (ROLE_PROFESSOR, "Professor"),
        (ROLE_ADMIN, "Admin"),
    )

    # rôle par défaut PROFESSOR
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_PROFESSOR)

    def is_professor(self) -> bool:
        return self.role == self.ROLE_PROFESSOR

    def is_admin_role(self) -> bool:
        return self.role == self.ROLE_ADMIN
