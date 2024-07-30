from django.db import models

# Create your models here.

'''
django model field :
    - html widget
    - validation
    - db size
'''
JOB_TYPE=(
    ('Full Time','Full Time'),    
    ('Part Time','Part Time'),
)


def image_upload(instance,filename):
    imagename,extension=filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)


class Job(models.Model):
    title=models.CharField(max_length=100)
    # location
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    description=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experince=models.IntegerField(default=1)
    category=models.ForeignKey('Categroy',on_delete=models.CASCADE)
    #image=models.ImageField(upload_to='jobs/')
    image=models.ImageField(upload_to=image_upload)
    
    def __str__(self) :
        return self.title
    
class Categroy(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self) :
        return self.name
    

class Apply(models.Model):
    