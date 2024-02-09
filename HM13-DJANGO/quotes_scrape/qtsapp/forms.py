from django.forms import ModelForm, CharField, TextInput, ModelChoiceField
from .models import Author, Quote

class AuthorForm(ModelForm):
    fullname = CharField(max_length=120, required=True, widget=TextInput)
    born_date = CharField(max_length=120, required=True, widget=TextInput)
    born_location = CharField(max_length=120, required=True, widget=TextInput)
    description = CharField(max_length=5000,required=True, widget=TextInput)

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

class QuoteForm(ModelForm):

    quote = CharField(min_length=5, max_length=2500, required=True, widget=TextInput())
    author = ModelChoiceField(queryset=Author.objects.all(), widget=TextInput())
    tags = CharField(max_length=500, required=True, widget=TextInput())
    
    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        if not tags:
            del self.cleaned_data['tags']
        else:
            tags_list = [tag.strip() for tag in tags.split(',') if tag.strip()]
            self.cleaned_data['tags'] = tags_list
        return tags_list
        
    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']
        # exclude = ['tags']


