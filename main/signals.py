def createGroupsAndPermissions(sender, **kwargs):
    from django.contrib.auth.models import Group, Permission    


    group, created = Group.objects.get_or_create(name='team_leader')  
    if created:
        group.permissions.add(Permission.objects.get(codename="add_project"))
        group.permissions.add(Permission.objects.get(codename="change_issue"))

    group, created = Group.objects.get_or_create(name='developer')  
    if created:
        group.permissions.add(Permission.objects.get(codename='add_issue'))