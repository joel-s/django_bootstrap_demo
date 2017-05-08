from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['topic'] = data['topic'].strip("/").replace("_", " ")
        return data

    # def get_context_data(topic):
    #     what = what.strip("/").replace("_", " ")
    #     context = {'topic': topic}
    #     return render(request, "main/about.html", context)
