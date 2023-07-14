from django import forms

class createNewIssue(forms.Form):
    title = forms.CharField(label="Title", max_length=64)
    description = forms.CharField(label="Description", max_length=256, widget=forms.Textarea())
    # date_created = forms.DateField(widget=forms.SelectDateWidget())
    
    STATUS = [
        ("P", "Pending"),
        ("I", "In Progress"),
        ("C", "Completed"),
    ]
    status = forms.CharField(label='Status',widget = forms.Select(choices=STATUS))
    
    TYPE = [
        ("B", "Bug"),
        ("F", "Feature"),
        ("T", "Task"),
    ]
    type = forms.CharField(label='Type', widget = forms.Select(choices=TYPE))
    