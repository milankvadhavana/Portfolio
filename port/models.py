from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class About(models.Model):
    name = models.CharField(max_length=100, default="Web Developer")
    birthday = models.DateField()
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    degree = models.CharField(max_length=100)
    freelance = models.CharField(max_length=50, choices=[("Available", "Available"), ("Not Available", "Not Available")])
    description_short = models.TextField(help_text="Short description for the 'About' section")
    # description_long = models.TextField(help_text="Longer description for additional details")
    image = models.ImageField(upload_to='about_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    year = models.CharField(max_length=20)  # Example: "2020-2023"
    institute_name = models.CharField(max_length=255)  # Example: "XYZ University"
    degree = models.CharField(max_length=255)  # Example: "Bachelor of Science in Computer Science"
    percentage = models.DecimalField(max_digits=5, decimal_places=2)  # Example: 83.45
    grade = models.CharField(max_length=5, blank=True, null=True)  # Example: "A+"
    class_name = models.CharField(max_length=50,blank=True, null=True)  # Example: "First Class"
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.year} - {self.institute_name}"
    

class Skills(models.Model):
    name = models.CharField(max_length=25)  # Corrected from 'nane' to 'name'
    skill_img = models.ImageField(upload_to='skills_images/')
    
    def __str__(self):
        return self.name  
    
class Certificate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(help_text="Short description for the about the certificate section")
    image = models.ImageField(upload_to='certificates/')

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    technology = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    client = models.CharField(max_length=100,blank=True, null=True)
    description = RichTextField(blank=True, null=False)
    project_url = models.URLField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='project_img/')
    
    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_img/')
    
    def __str__(self):
        return f"Image for {self.project.title}"



