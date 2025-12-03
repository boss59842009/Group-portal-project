from django.forms import ModelForm, TextInput, Textarea, Select, DateField, DateInput, FileInput, Form, ChoiceField
from forum.models import Thread, Messages

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ["name", "description", "icon",]

        widgets = {
            "name": TextInput(attrs={"class": "form-control", "placeholder": "Назва треду", "required": True}),
            "description": Textarea(attrs={"class": "form-control", "placeholder": "Опис треду", "required": True}),
            "icon": FileInput(attrs={"class": "form-control", "required":False}),

        }

class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ["text"]

        widgets = {
            "text": Textarea(attrs={"class": "form-control", "placeholder": "Текст коментарю", "required": True}),
        }

class ThreadsFilterForm(Form):
    pass
