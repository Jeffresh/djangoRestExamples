from django.shortcuts import render
from django.views.generic.base import View
from rest_framework.parsers import JSONParser
import json
import io
import requests


class SnippetList(View):
    def get(self, request):
        snippets_request = requests.get("http://127.0.0.1:8000/api/snippets/")
        stream_snippets = io.BytesIO(snippets_request.content)
        deserialized_snippets = JSONParser().parse(stream_snippets)

        data_snippets = []

        for batch in deserialized_snippets['results']:
            user_request = requests.get(batch['owner'])
            stream_user = io.BytesIO(user_request.content)
            deserialized_user = JSONParser().parse(stream_user)

            data_snippets.append({'user': deserialized_user['username'], 'title': batch['title'], 'code': batch['code']})

        return render(request, 'snippets.html', {'snippets': data_snippets})
