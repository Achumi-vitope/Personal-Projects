from django.shortcuts import render
from menu import menu_items
from ai import text

# Create your views here.

label_tags = [
    'College',
    'Business',
    'Professional'
]


def index(request):
    question = 'Example: Write an essay on grumpy cat.'
    if request.method == 'POST':
        inp = request.POST['input']
        proficiency = request.POST['proficiency'] if 'proficiency' in request.POST else 'College'
        limit = request.POST['wordLimit'] if 'proficiency' in request.POST else '300'
        question = request.POST['input']
        get_response = text(inp, proficiency, limit)
        return render(request, 'content_gen/index.html', {
        'value':get_response,
        'question':question,
        'label':label_tags
        })
    else:
        return render(request, 'content_gen/index.html', {
        'question':question,
        'label':label_tags
    })
        
