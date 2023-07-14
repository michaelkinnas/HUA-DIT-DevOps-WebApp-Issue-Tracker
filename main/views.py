from django.shortcuts import render
from .models import Issue

# Create your views here.
def home(request):
    issues = Issue.objects.all()
    return render(request, "main/overview_cards.html", {"issues":issues})

def issue(request, id):
    if request.method == 'POST':
        status = request.POST.get('status')
        dev = request.POST.get('assign_to')
        issue = Issue.objects.get(id=id)
        issue.status = status
        issue.save()
        #implement assign to developer. must add the field to model aswell.
    issue = Issue.objects.get(id=id)
    return render(request, "main/details.html", {"issue":issue})

def create(request):
    pass