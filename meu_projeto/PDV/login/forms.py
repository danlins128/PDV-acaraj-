from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fiels = ['nome', 'preco', 'quantidade_em_estoque']