from django import forms

g=[('MALE','MALE'),('FEMALE','FEMALE')]
c=[('python','python'),('django','django'),('sql','sql')]

class RegistraionForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    courses=forms.MultipleChoiceField(choices=c)
    

    

