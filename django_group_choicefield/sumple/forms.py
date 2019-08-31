from django import forms

from .fields import GroupedModelChoiceField
from .models import ColorType, Expense


class ExpenseForm(forms.Form):
    COLORS = (
        (11, 'SALT & PEPPER'),
        (12, 'DARK GREY'),
        (21, 'GREY'),
        (22, 'CHOCOLATE'),
        (23, 'BROWN'),
        (31, 'CINNAMON'),
        (32, 'DARK CINNICOT'),
    )
    name = forms.DecimalField()
    birthday = forms.DateField()
    ColorType = forms.ChoiceField(choices=COLORS)


class GroupedExpenseForm(forms.Form):
    COLORS = (
        ('Popular', (
            (11, 'SALT & PEPPER'),
            (12, 'DARK GREY'),
        )),
        ('GrayScale', (
            (21, 'GREY'),
            (22, 'CHOCOLATE'),
            (23, 'BROWN'),
        )),
        ('WhiteScale', (
            (31, 'CINNAMON'),
            (32, 'DARK CINNICOT'),
        )),
    )
    name = forms.DecimalField()
    birthday = forms.DateField()
    colortype = forms.ChoiceField(choices=COLORS)


class ExpenseModelForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('name', 'birthday', 'colortype')


class GroupedExpenseModelForm(forms.ModelForm):
    colortype = GroupedModelChoiceField(
        queryset=ColorType.objects.exclude(parent=None), choices_groupby='parent')

    class Meta:
        model = Expense
        fields = ('name', 'birthday', 'colortype')
