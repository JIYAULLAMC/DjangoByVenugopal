from django import forms



class registerform(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter the username'}),max_length=20,min_length=3,required=True,label='USERNAME',help_text='plz enter the username')
    firstname=forms.CharField()
    age=forms.IntegerField(max_value=65,min_value=10)
    email=forms.EmailField()
    phone=forms.IntegerField(min_value=6000000000,max_value=9999999999)
    c=[['male','male'],['Female','Female']]
    gender=forms.ChoiceField(choices=c,widget=forms.RadioSelect)
    date=forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))




class registform(forms.Form):
    date=forms.DateField()
    date1=forms.DateField(widget=forms.TimeInput)
    date2=forms.DateField(widget=forms.DateTimeInput)
    date3=forms.DateField(widget=forms.SelectDateWidget)
    li=['2019','2020','2021']
    date4=forms.DateField(widget=forms.SelectDateWidget(years=li))
    date5=forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    
class registform(forms.Form):
    c=[['male','male'],['Female','Female']]
    gender=forms.ChoiceField(choices=c)
    gender1=forms.ChoiceField(choices=c,widget=forms.CheckboxInput)
    gender2=forms.ChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    gender3=forms.ChoiceField(choices=c,widget=forms.RadioSelect)
    gender4=forms.MultipleChoiceField(choices=c)
    #gender5=forms.ModelChoiceField()



class regform(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    name1=forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':10}))
    name2=forms.CharField(widget=forms.PasswordInput)
    name3=forms.CharField(widget=forms.EmailInput)
    name4=forms.CharField(widget=forms.DateInput)
    name5=forms.CharField(widget=forms.DateTimeInput)
    name6=forms.CharField(widget=forms.TimeInput)
    name7=forms.CharField(widget=forms.URLInput)
    name8=forms.CharField(widget=forms.NumberInput)

class loginform(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField()
    c=[['male','male'],['Female','Female']]
    gender=forms.ChoiceField(choices=c)
    password=forms.CharField(widget=forms.PasswordInput)
    agree=forms.BooleanField()
    date=forms.DateField()
    img=forms.ImageField()
    file=forms.FileField()
    a=forms.DecimalField()
    b=forms.DurationField()
    
    d=forms.GenericIPAddressField()
    e=forms.HiddenInput()
    f=forms.JSONField()
    g=forms.MultiValueField(fields=[forms.CharField(),forms.IntegerField()],)
    h=forms.NullBooleanField()
    i=forms.RegexField(regex='[0-9]{10}')
    j=forms.SplitDateTimeField()
    k=forms.TimeField()
    l=forms.TypedChoiceField(choices=c)
    m=forms.TypedMultipleChoiceField(choices=c)
    n=forms.URLField()
    o=forms.UUIDField()
