from django.forms import ModelForm, CharField, TextInput
from .models import Note, Tag

'''
Форми Django - це клас, поля якого зіставляються з елементами html-форми. 
Клас forms має різні поля для обробки різних типів даних. Наприклад, CharField, DateField тощо.
'''
class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']


class NoteForm(ModelForm):

    name = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    description = CharField(min_length=10, max_length=150, required=True, widget=TextInput())

    class Meta:
        model = Note
        fields = ['name', 'description']
        exclude = ['tags']  # виключили з перевірки форми теги, оскільки це зв'язок багато-до-багатьох і
        # будемо його обробляти в особливий спосіб
        