from events_calendar.models import Event
from django.forms import ModelForm, Form, TextInput, Textarea, Select, DateField, DateInput, FileInput, ChoiceField, TimeInput

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "date_start", "date_end", "time_start", "time_end"]

        widgets = {
            "title": TextInput(attrs={"class": "form-control", "placeholder": "Заголовок", "required": True}), 
            "description": Textarea(attrs={"class": "form-control", "placeholder": "Опис", "required": True}),
            "date_start": DateInput(attrs={"class": "form-control", "required": True, "type": "date"}),
            "date_end": DateInput(attrs={"class": "form-control", "required": True, "type": "date"}),
            "time_start": TimeInput(attrs={"class": "form-control", "required": True, "type": "time"}),
            "time_end": TimeInput(attrs={"class": "form-control", "required": True, "type": "time"})
        }

# class EventsFilterForm(Form):
#     FILTER_MONTH = [
#         ("January", "Січень"),
#         ("February", "Лютий"),
#         ("March", "Березень"),
#         ("April", "Квітень"),
#         ("May", "Травень"),
#         ("June", "Червень"),
#         ("July", "Липень"),
#         ("Augest", "Серпень"),
#         ("September", "Вересень"),
#         ("October", "Жовтень"),
#         ("November", "Листопад"),
#         ("December", "Грудень"),
#     ]

# month = ChoiceField(choices = FILTER_MONTH, )