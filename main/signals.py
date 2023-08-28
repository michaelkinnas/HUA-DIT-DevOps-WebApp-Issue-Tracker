def createGroupsAndPermissions(sender, **kwargs):
    from django.contrib.auth.models import Group, Permission

    group, created = Group.objects.get_or_create(name='team_leader')  
    if created:
        group.permissions.add(Permission.objects.get(codename="add_project"))
        group.permissions.add(Permission.objects.get(codename="change_issue"))

    group, created = Group.objects.get_or_create(name='developer')  
    if created:
        group.permissions.add(Permission.objects.get(codename='add_issue'))



def createTestUsers(sender, **kwargs):
    from django.contrib.auth.models import User, Group

    developer1 = User.objects.create_user('developer1', 'dev1@company.com', 'pass12345')
    if not developer1:
        raise Exception("Error creating user")
    
    group = Group.objects.get(name='developer')
    developer1.groups.add(group)

    leader1 = User.objects.create_user('leader1', 'lead1@company.com', 'pass12345')
    if not developer1:
        raise Exception("Error creating user")
    
    group = Group.objects.get(name='developer')
    leader1.groups.add(group)
    group = Group.objects.get(name='team_leader')
    leader1.groups.add(group)
