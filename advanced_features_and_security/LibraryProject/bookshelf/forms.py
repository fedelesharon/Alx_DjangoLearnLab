from django import forms

# Example: A search form to search for books
class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=True, label='Search Books')

    def clean_query(self):
        query = self.cleaned_data.get('query')
        # Optional: Add validation or sanitization logic here
        return query
