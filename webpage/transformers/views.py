from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def main(request):
    title = 'Main Page'

    return render(request,
                  'transformers/main.html',
                  {'title': title})


def singleview(request):
    singleview = {
        'Transformer_Loc': 'T 8181',  # Put your name here
        'SKU': '91350',  # Put your country here
    }
    context = {'Transformer Loc': singleview,
               'title': 'Single Transformer View'}

    return render(request,
                  'transformers/user_info.html',
                  context)
