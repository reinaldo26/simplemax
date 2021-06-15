from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Client')
    age = models.PositiveIntegerField()
    birthdate = models.DateField()
    cpf = models.CharField(max_length=11)
    adress = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    complement = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    cep = models.CharField(max_length=9)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2, default='SP', choices=(
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
)

    def __str__(self):
        return f'{self.client.first_name} {self.client.last_name}'


    def clean(self):
        pass

    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
