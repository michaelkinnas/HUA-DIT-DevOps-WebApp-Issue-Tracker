from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from .models import Issue, Project
from .forms import createNewIssue

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

def create_project(request):
    pass

def create_issue(request, project_id):
    if request.method == "POST":
        form = createNewIssue(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            date_created = datetime.datetime.now()
            status = form.cleaned_data["status"]
            type = form.cleaned_data["type"]
            project = Project.objects.get(id=project_id)
           
            issue = Issue(title=title, description=description, date_created=date_created, status=status, type=type, project=project)
            issue.save()
            return HttpResponseRedirect(f"/issues/{project_id}")
    else: 
        form = createNewIssue() #in case of GET request, default method is GET
    return render(request, "main/create_issue.html", {"form":form, "project_id":project_id})
    