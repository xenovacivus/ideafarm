# Create your views here.
from django.http import HttpResponse
from content.models import Concept
from django.template import Context, loader

def index(request):
    concept_list  = Concept.objects.all()
    # output_string = "The content items are: "
    # for content_item in content_items:
    #     output_string = "{0}, {1}".format (output_string, content_item)
    t = loader.get_template ('content/index.html')
    c = Context ({'concept_list': concept_list,})
    return HttpResponse (t.render(c))
    # return HttpResponse("Hello, you've reached a page!  WHEEEE!\n{0}".format (output_string))

