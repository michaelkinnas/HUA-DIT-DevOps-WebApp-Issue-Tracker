from django.shortcuts import render
from .models import Issue, Project

# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, "main/projects.html", {"projects":projects})

def issues(request, project_id):
    project = Project.objects.get(id=project_id)    
    return render(request, "main/issues.html", {"project":project})

def issue(request, issue_id):
    if request.method == 'POST':
        status = request.POST.get('status')
        dev = request.POST.get('assign_to')
        issue = Issue.objects.get(id=issue_id)
        issue.status = status
        issue.save()
        #implement assign to developer. must add the field to model aswell.
    issue = Issue.objects.get(id=issue_id)  
    return render(request, "main/details.html", {"issue":issue})

def create(request):
    pass