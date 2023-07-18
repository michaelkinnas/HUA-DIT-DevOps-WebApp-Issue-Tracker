from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Issue, Project
from .forms import createNewIssue, createNewProject, RegisterForm
import datetime

# Create your views here.
@login_required(login_url="/login")
def home(request):   
    projects = Project.objects.all()
    return render(request, "main/projects.html", {"projects":projects}) 
        
@login_required(login_url="/login")
def issues(request, project_id):
    project = Project.objects.get(id=project_id)    
    return render(request, "main/issues.html", {"project":project})

#TODO Allow only team leaders to change details of issue
@login_required(login_url="/login")
def issue(request, issue_id):
    if request.method == 'POST':
        issue = Issue.objects.get(id=issue_id)

        status = request.POST.get('status')
        assigned_to = request.POST.get('assign_to')

        if not status == '0':
            issue.status = status

        if not assigned_to == '0':
            issue.assigned_to = User.objects.get(id=assigned_to)

        issue.save()
        
    issue = Issue.objects.get(id=issue_id)
    users = User.objects.all() #TODO Get only users belonging to developer group
    return render(request, "main/details.html", {"issue":issue, "users":users})

@login_required(login_url="/login")
def create_project(request):
    if request.method == "POST":
        form = createNewProject(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            project = Project(title=title, description=description)
            project.save()
            return redirect(f"/issues/{project.id}")
    else: #if method==GET
        form = createNewProject()
    return render(request, "main/create_project.html", {"form":form})
    
@login_required(login_url="/login")
def create_issue(request, project_id):
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
            return redirect(f"/issues/{project_id}")
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