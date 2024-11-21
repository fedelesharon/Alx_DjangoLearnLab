from django import forms

# Example: A simple form for user input (e.g., a book form)
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Name')
    email = forms.EmailField(required=True, label='Email')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Message')

    def clean_message(self):
        message = self.cleaned_data.get('message')
        # Optional: Add validation or sanitization logic here
        return message
