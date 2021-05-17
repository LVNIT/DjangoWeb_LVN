from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    full_name = forms.CharField(label='Full name:', help_text='Required', max_length=200,widget=forms.TextInput(
                                attrs={'class': 'form-control ', 'placeholder': 'Long'
                                       }
                                ))
    phone = forms.CharField(label='Phone:', help_text='Required', max_length=15,widget=forms.TextInput(
                            attrs={'class': 'form-control ', 'placeholder': '45438484567456'
                                   }
                            ))
    address = forms.CharField(label='Address', help_text='Required', max_length= 200,widget=forms.TextInput(
                              attrs={'class': 'form-control ', 'placeholder': '42 ds5'
                                     }
                              ))
    city = forms.CharField(label='City:',  help_text='Required', max_length= 100,widget=forms.TextInput(
                           attrs={'class': 'form-control ', 'placeholder': 'HCM'
                                  }
                           ))

    class Meta:
        model = Order
        fields = ['full_name', 'phone', 'address', 'city']


