from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    created_at = models.DateField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.project.title}"
