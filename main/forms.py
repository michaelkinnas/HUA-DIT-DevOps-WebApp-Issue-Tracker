from django import forms

class createNewIssue(forms.Form):
    title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}))
    description = forms.CharField(max_length=256, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}))
    # date_created = forms.DateField(widget=forms.SelectDateWidget())
    
    # STATUS = [
    #     ("P", "Pending"),
    #     ("I", "In Progress"),
    #     ("C", "Completed"),
    # ]
    # status = forms.CharField(label='Status',widget = forms.Select(choices=STATUS))
    
    TYPE = [
        ("B", "Bug"),
        ("F", "Feature"),
        ("T", "Task"),
    ]
    type = forms.CharField(label='Type', widget = forms.Select(choices=TYPE, attrs={'class':'form-select'}))
    
class createNewProject(forms.Form):
    title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}))
    description = forms.CharField(max_length=256, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}))