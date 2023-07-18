from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import datetime
from .models import Issue, Project
from .forms import createNewIssue, createNewProject, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    
    projects = Project.objects.all()
    return render(request, "main/projects.html", {"projects":projects}) 
        

def issues(request, project_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    project = Project.objects.get(id=project_id)    
    return render(request, "main/issues.html", {"project":project})

#TODO Allow only team leaders to change details of issue
def issue(request, issue_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    
    if request.method == 'POST':
        status = request.POST.get('status')
        assigned_to = request.POST.get('assign_to')
        issue = Issue.objects.get(id=issue_id)
        issue.status = status
        issue.assigned_to = User.objects.get(id=assigned_to)
        issue.save()
    issue = Issue.objects.get(id=issue_id)
    users = User.objects.all() #TODO Get only users belonging to developer
    return render(request, "main/details.html", {"issue":issue, "users":users})

def create_project(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    
    if request.method == "POST":
        form = createNewProject(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            project = Project(title=title, description=description)
            project.save()
            return HttpResponseRedirect(f"/issues/{project.id}")
    else: #if method==GET
        form = createNewProject()
    return render(request, "main/create_project.html", {"form":form})
    

def create_issue(request, project_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    
    if request.method == "POST":
        print(request.user)

        form = createNewIssue(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            date_created = datetime.datetime.now()
            status = "P"
            type = form.cleaned_data["type"]
            project = Project.objects.get(id=project_id)
            created_by = request.user
            issue = Issue(title=title, description=description, date_created=date_created, status=status, type=type, project=project, created_by=created_by)
            issue.save()
            return HttpResponseRedirect(f"/issues/{project_id}")
    else: #if method==GET
        form = createNewIssue()
    return render(request, "main/create_issue.html", {"form":form, "project_id":project_id})
    
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) #auto login user after registration
        return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form':form})