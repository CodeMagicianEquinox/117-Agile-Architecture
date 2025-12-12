from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='projects/')
    respository = models.URLField()
    skills = models.ManyToManyField(Skill)
    link = models.URLField(blank=True, null=True)

    # ✅ New field to group projects into sections
    category = models.CharField(
        max_length=50,
        choices=[
            ("Frontend", "Frontend"),
            ("Capstone", "Capstone"),
            ("Backend", "Backend"),
            ("Fullstack", "Fullstack"),
        ],
        default="Frontend"
    )

    def __str__(self):
        return f'{self.title} ** {self.year}'
