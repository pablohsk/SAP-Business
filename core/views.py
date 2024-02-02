from django.shortcuts import render
from django.views import View


class SuaView(View):
    def get(self, request):
        # Lógica da view para manipular solicitações GET
        return render(request, 'sua_template.html', {'alguma_variavel': 'algum_valor'})