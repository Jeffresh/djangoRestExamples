from django.shortcuts import render
from django.views.generic.base import View
import json
import requests


class SnippetList(View):
    def get(self, request):
        snippets = requests.get("http://127.0.0.1:8000/api/snippets/")

        return render(request, 'snippets.html', {'snippets': snippets.text})
