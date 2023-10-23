from django.shortcuts import render
from django.http import Http404
from . import util
from django.core.files.storage import default_storage
from markdown2 import Markdown
import random

def md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
       
    })

def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        raise Http404("La página solicitada no se encontró.")
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
    })

def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = md_to_html(entry_search)
        if html_content is not None:
            return render(request, "encyclopedia/entry.html",{
                "title": entry_search,
                "content": html_content
                })
        else:
            allEntries = util.list_entries()
            recommendation = []
            for entry in allEntries:
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)
            return render(request, "encyclopedia/search.html", {
                "recommendation": recommendation
            })     


def rand(request):
    allEntries = util.list_entries()
    randomEntry = random.choice(allEntries)
    html_content = md_to_html(randomEntry)
    return render(request, "encyclopedia/entry.html",{
        "title": randomEntry,
        "content": html_content
        })


def create_page_template(request):
    return render(request, "encyclopedia/create_page.html")


def create_page(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        return render(request, "encyclopedia/entry.html",{
            "title": title,
            "content": content
            })

def edit_entry(request, title):
    if request.method == "POST":
        content = request.POST['content']
        util.save_entry(title, content)
        return render(request, "encyclopedia/entry.html",{
            "title": title,
            "content": content
            })

def eliminate_entry(request, title):
    if request.method == "POST":
        util.delete_entry(title)
        return render(request, "encyclopedia/index.html",{
            "entries": util.list_entries()
            })