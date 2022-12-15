from msilib.schema import Class
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.

def query(request):
    return render(request, 'engine/home.html')


def results(request):
    if request.method == "POST":
        query = request.POST.get('search')
        if query == "":
            return render(request, 'engine/home.html')
        else:

            #results = []
            #page = requests.get('https://search17.lycos.com/web/?q='+query).text
            #soup = BeautifulSoup(page,'lxml')

            results = []
            page = requests.get('https://datasetsearch.research.google.com/search?src=0&query='+query).text
            soup = BeautifulSoup(page,'lxml')

            ##google dataset test in large right box - not working
            #listingTitle = soup.find_all(class_="kCClje")
            #for content in listingTitle:
            #    title = content.find(class_='iKH1Bc').text
            #    description = content.find(class_='p86njf').text
            #    results.append((title,description))

            #test for button properties - googe datasets - works!
            listingTitle = soup.find_all(class_="UnWQ5")
            for content in listingTitle:
                title = content.find(class_='iKH1Bc').text
                description = content.find(class_='iKH1Bc').text
                url = content.find(class_='iW1HZe').text
                results.append((title,description,url))

            ##basic lycos search - works
            #listi = soup.find_all(class_="result-item")
            #for content in listi:
            #    title = content.find(class_='result-title').text
            #    description = content.find(class_='result-description').text
            #    link = content.find(class_='result-link').text
            #    url = content.find(class_='result-url').text
            #    results.append((title,description,url))


            ##basic lycos search recommended - works
            #listings = soup.find_all(class_="results search-related")
            #for content in listings:
            #    t = content.find(class_='rs-title').text
            #    de = content.find(class_='rs-list').text
            #    results.append((t, de))


            ##----------------------------KAGGLE SEARCH--------------------------------#
            #results = []
            #page = requests.get('https://www.kaggle.com/datasets?search='+query).text
            #soup = BeautifulSoup(page,'lxml')
            #listingTitle = soup.find_all(class_="sc-jfmDQi hfJycS")
            #for content in listingTitle:
            #    title = content.find(class_='sc-iBkjds sc-fLlhyt sc-fbPSWO uVZhN izULIq A-dENW').text
            #    description = content.find(class_='sc-jIZahH sc-himrzO sc-fXynhf kdTVzc glCpMy ctwKCt').text
            ##    url = content.find(class_='sc-lbOyJj eeGduD').text
            #    results.append((title,description))

            context = {
                'results':results
            }
            return render(request, 'engine/results.html', context)
    else:
        return render(request, 'engine/results.html')

def about(request):
    return render(request, 'engine/about.html')