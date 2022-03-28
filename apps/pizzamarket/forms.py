from django import forms


class CommentUserForm(forms.Form):
    text = forms.CharField(required=True)
    name = forms.CharField(required=True,max_length=100)
    email = forms.CharField(required=False)


class EmailPublicForm(forms.Form):
    name=forms.CharField(max_length=50)
    email=forms.EmailField()





   # class Meta:
   #      model=CommentUser
   #      fields = ('name','message','email')
