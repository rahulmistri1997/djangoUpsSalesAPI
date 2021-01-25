from django.shortcuts import render
from django.http import HttpResponse
import requests
from lxml import html
import json

def index(request):
    return HttpResponse("Please enter the tracking Number After the / in the URL.")

def detail(request, trackingNumber):
    trackingNum = test(trackingNumber)
    return HttpResponse(trackingNum)

def test(number):
    url = 'https://www.upspostsaleslogistics.com/cfw/trackOrder.action'
    myobj = {'trackNumber': number} #77345621

    finalreq = requests.post(url, data = myobj)
    tree = html.fromstring(finalreq.text)
    trackinginfo = tree.xpath('//div[@class="indent"]/text()')

    toprocesslist = []
    finaldict = {}

    for each in trackinginfo:
        a = each.strip()
        toprocesslist.append(a)

    finallist = [x.split(":") for x in toprocesslist]

    for each in finallist:
        if len(each) > 1:
            finaldict[each[0]] = each[1]
        else:
            finaldict[each[0]] = ""

    outputJson = json.dumps(finaldict)
    return outputJson