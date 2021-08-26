from django import forms
from .models import Resume

GENDER_CHOICES=[
    
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')

]


JOB_CHOICES=[
    
    ('Mumbai','Mumbai'),
    ('Banglore','Banglore'),
    ('Pune','Pune'),
    ('Hyderabad','Hyderabad'),
    ('Delhi','Delhi')

]

class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(label='Preffered Job Locations', choices=JOB_CHOICES, widget=forms.CheckboxSelectMultiple)
    class Meta:
        
        model=Resume
        fields='__all__'

        labels={'name':'Full Name','dob':'Date Of Birth','pin':'Pin Code','mobile':'Mobile No',
                'profile_image':'Profile Image','my_file':'Document','email':'Email Id'}
        
        widgets={
            
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),







        }