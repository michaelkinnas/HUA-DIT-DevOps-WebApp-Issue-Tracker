from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import Issue, Project
from .forms import createNewIssue, createNewProject, RegisterForm
import datetime

#TODO check what ip does request.META['HTTP_ORIGIN'] returns when deployed to vms
#TODO implement sending a welcoming email to new users when they register

# Create your views here.
@login_required(login_url="/login")
def home(request):   
    projects = Project.objects.all()
    return render(request, "main/projects.html", {"projects":projects}) 
        
@login_required(login_url="/login")
def issues(request, project_id):
    project = Project.objects.get(id=project_id)    
    return render(request, "main/issues.html", {"project":project})


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
        
        # send email to user        
        topic = 'You have been assigned an issue'     
        
        context = {
            'issue_id':issue.id,
            'issue_title':issue.title,
            'issue_description':issue.description,
            'dev_username': issue.assigned_to.username,
            'leader_username': request.user.username,
            'issue_link': request.META['HTTP_ORIGIN'] + '/issue/' + str(issue.id)
        }
        # print(request.META['HTTP_ORIGIN'])
        
        html_message = render_to_string('email/email.html', context)
        plain_message = strip_tags(html_message)
        sender = request.user.email
        receivers = [issue.assigned_to.email]

        try:
            send_mail(topic, plain_message, sender, receivers, fail_silently=False, html_message=html_message)
        except ConnectionError:
            # return HttpResponse('Invalid header found.')
            print("Email was not send. Could not connect to SMTP server")
        issue.save()
        
    issue = Issue.objects.get(id=issue_id)
    users = User.objects.all()
    return render(request, "main/details.html", {"issue":issue, "users":users})


@login_required(login_url="/login")
@permission_required('main.add_project', raise_exception=True)
def create_project(request):
    if request.method == "POST":
        # print(request.user.has_perm('main.change_issue'))
        # if request.user.has_perm('main.change_issue'):
            
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
@permission_required('main.add_issue', raise_exception=True)
def create_issue(request, project_id):
    if request.method == "POST":
        # print(request.user)

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
    

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            # user = form.cleaned_data
            group = Group.objects.get(name='developer')
            user.groups.add(group)
            
            login(request, user) #auto login user after registration

            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form':form})