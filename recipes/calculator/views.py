from pprint import pprint

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

#venv/scripts/activate


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}



def get_omlet(request):
    quan = request.GET.get('servings', 1)
    rec = {}
    quan = int(quan)
    rec = DATA["omlet"]
    in1 = rec['яйца, шт']*quan
    in2 = rec['молоко, л']*quan
    in3 = rec['соль, ч.л.']*quan
    context = {
        'яйца': in1,
        'молоко': in2,
        'соль': in3
        }
    return render(request, "calculator/omlet.html", context)

def get_pasta(request):
    quan = request.GET.get('servings', 1)
    rec = {}
    quan = int(quan)
    rec = DATA["pasta"]
    print(rec)
    in1 = rec['макароны, г'] * quan
    in2 = rec['сыр, г'] * quan
    print(in2, in1)
    context = {
        'макароны': in1,
        'сыр': in2
    }
    pprint(context)

    return render(request, "calculator/pasta.html", context)

def get_buter(request):
    quan = request.GET.get('servings', 1)
    rec = {}
    quan = int(quan)
    rec = DATA["buter"]
    in1 = rec['хлеб, ломтик']*quan
    in2 = rec['колбаса, ломтик']*quan
    in3 = rec['сыр, ломтик']*quan
    in4 = rec['помидор, ломтик'] * quan
    context = {
        'хлеб': in1,
        'колбаса': in2,
        'сыр': in3,
        'помидор': in4
        }
    return render(request, "calculator/buter.html", context)


