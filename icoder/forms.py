from django import forms



#class PostForm(forms.Form):
#    sno = forms.AutoField(primary_key=True)
#    title = forms.CharField(max_length=255)
#    content = forms.TextField()
#    author = forms.CharField(max_length=13)
#    slug = forms.CharField(max_length=130)
#    timeStamp = forms.DateTimeField(blank=True)
#    views = forms.IntegerField(default=0)
#    image1 = forms.ImageField(upload_to="images", default="")
#    image2 = forms.ImageField(upload_to="images", default="")

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields ='__all__'