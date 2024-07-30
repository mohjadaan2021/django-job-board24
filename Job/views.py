from django.shortcuts import render
from .models import Job
from .form import ApplyForm
# Create your views here.

def job_list(request):
    job_list=Job.objects.all()
    context={'jobs':job_list} # template name used in job.html page
    return render(request,'job/job_list.html',context)

def job_detail(request,id):
    job_detail=Job.objects.get(id=id)

    if request.method=='POST':
        pass
    else:
        form=ApplyForm()

    context={'job':job_detail,'form':form}
    return render(request,'job/job_detail.html',context)