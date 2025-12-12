from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    year = models.CharField(max_length=4)
    url = models.URLField()
    image = models.ImageField(upload_to='projects/')
    
    # store skills as: "HTML, CSS, JavaScript"
    skills = models.CharField(max_length=255, help_text="Comma-separated list of skills")

    def skill_list(self):
        return [skill.strip() for skill in self.skills.split(',')]

    def __str__(self):
        return self.title
