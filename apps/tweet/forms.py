from django import forms


class GetTweetsByUserForm(forms.Form):

    twitter_username = forms.CharField(max_length=30, required=True)

    def save(self, *args, **kwargs):
        return self.cleaned_data['twitter_username']
