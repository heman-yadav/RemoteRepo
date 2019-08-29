from django import forms

# we are declaring here fields for form
class FeedbackForm(forms.Form):
    name = forms.CharField(
        label='Enter Your name',
        widget=forms.TextInput(
            attrs={
                'class':'from-control',
                'placeholder':'Your name'
            }
        )
    )

    rating = forms.IntegerField(
        label='Enter Your Rating',
        widget=forms.NumberInput(
            attrs={
                'class': 'from-control',
                'placeholder': 'Your Rating'
            }
        )
    )

    feedback = forms.CharField(
        label='Enter Your Feedback',
        widget=forms.TextInput(
            attrs={
                'class': 'from-control',
                'placeholder': 'Your feedback here'
            }
        )
    )