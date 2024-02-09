from django.shortcuts import get_object_or_404, redirect, render
from .forms import QuoteForm, AuthorForm
from .models import Author, Quote

# Create your views here.
def main(request):
    quotes = Quote.objects.all()
    return render(request, 'qtsapp/index.html', {"quotes": quotes})


def author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="qtsapp:main")
        else:
            return render(request, "qtsapp/author.html", {"form": form})

    return render(request, "qtsapp/author.html", {"form": AuthorForm()})

def quote(request):
    authors = Author.objects.all()
    # tags = Tag.objects.all()


    if request.method == "POST":
        form = QuoteForm(request.POST)

        if form.is_valid():
            new_quote = form.save()

            return redirect(to="qtsapp:main")
        else:
            return render(request, "qtsapp/quote.html", {"authors": authors, "form": form}) 

    return render(request, "qtsapp/quote.html", {"authors": authors, "form": QuoteForm()}) 

def detail(request, quote_id):
    print("quote_id")
    quote = get_object_or_404(Quote, pk=quote_id)
    author = Author.objects.get(id=quote.author_id)

    return render(request, "qtsapp/detail.html", {"quote": quote, "author": author})

def about_author(request, author_id):
    author = Author.objects.get(id=author_id)
    
    return render(request, 'qtsapp/about_author.html', {"author": author})