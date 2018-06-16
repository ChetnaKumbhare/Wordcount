from django.http import HttpResponse
import operator
from django.shortcuts import render
def hook(request):
    return render(request, 'Chetna.html')
def submit(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wd_dic = {}
    for word in wordlist:
        if word in wd_dic:
            wd_dic[word]+= 1
        else:
                wd_dic[word] = 1
    sortedwords=sorted(wd_dic.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'submit.html',{'fulltext':fulltext,'count':len(wordlist),'wd_dic':sortedwords})

def about(request):
    return render(request, 'about.html')
