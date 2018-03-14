from django.template import loader
from .models import Item, Review
from django.http import HttpResponse

# Create your views here.
def index(request):
    items = Item.objects.all()
    template = loader.get_template('posts/index.html')
    context = {
        'items': items,
    }
    return HttpResponse(template.render(context, request))

def details(request, item_id):
    return HttpResponse("<h1>Details for item: " + str(item_id) + "</h2>")