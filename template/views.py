from django.shortcuts import render
from django.views.generic.base import TemplateView
import requests

from template.models import MeritListEntry
# Create your views here.
class IndexView(TemplateView):
    template_name = "template/index.html"

# class IndexView(TemplateView):
#     template_name = "template/index.html"

class Cycke6View(TemplateView):
    template_name = "template/cycke6.html"

class DatacollectionView(TemplateView):
    template_name = "template/datacollection.html"

class NtrcaView(TemplateView):
    template_name = "template/ntrca-recruitment-cycle.html"


class SearchView(TemplateView):
    template_name = "template/search2c7b.html"

# class TableView(TemplateView):
#     template_name = "template/table.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # First API
#         merit_url = "http://ngi.teletalk.com.bd/ntrca/merit/load-merit-list.php?subject=325&level=3"
#         merit_payload = {"draw": "1"}
#         try:
#             merit_response = requests.post(merit_url, data=merit_payload)
#             merit_response.raise_for_status()
#             context["merit_data"] = merit_response.json()
#         except requests.RequestException as e:
#             context["merit_data"] = {"error": str(e)}

#         # Second API
#         posts_url = "http://ngi.teletalk.com.bd/ntrca/merit/get-posts-subjects.php?type=post&level=4"
#         try:
#             posts_response = requests.get(posts_url)
#             posts_response.raise_for_status()
#             context["posts_data"] = posts_response.json()
#         except requests.RequestException as e:
#             context["posts_data"] = {"error": str(e)}

#         return context

class TableView(TemplateView):
    template_name = "template/table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        custom_data = list(MeritListEntry.objects.values())  # convert queryset to list of dicts
        level = self.request.GET.get("level", "3")
        subject = self.request.GET.get("subject", "325")
        draw = self.request.GET.get("draw", "1")  # Default to page 1

        merit_url = f"http://ngi.teletalk.com.bd/ntrca/merit/load-merit-list.php?subject={subject}&level={level}"
        merit_payload = {"draw": draw}

        try:
            merit_response = requests.post(merit_url, data=merit_payload)
            merit_response.raise_for_status()
            merit_json = merit_response.json()

            # Merge custom_data into merit_data['data'] if it's a list
            if "data" in merit_json and isinstance(merit_json["data"], list):
                merit_json["data"].extend(custom_data)  # append your data
            else:
                merit_json["custom_data"] = custom_data  # fallback to new key

            context["merit_data"] = merit_json
        except requests.RequestException as e:
            context["merit_data"] = {"error": str(e)}

        posts_url = f"http://ngi.teletalk.com.bd/ntrca/merit/get-posts-subjects.php?type=post&level={level}"
        try:
            posts_response = requests.get(posts_url)
            posts_response.raise_for_status()
            context["posts_options"] = posts_response.text
        except requests.RequestException as e:
            context["posts_options"] = f'<option value="">Error loading subjects: {str(e)}</option>'
        print(context)
        return context

