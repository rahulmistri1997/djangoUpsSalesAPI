import requests
from lxml import html
import json

url = 'https://www.upspostsaleslogistics.com/cfw/trackOrder.action'
myobj = {'trackNumber': 77345621}

x = requests.post(url, data = myobj)

tree = html.fromstring(x.text)
buyers = tree.xpath('//div[@class="indent"]/text()')
# print(x.text)
# print(buyers)
alist = []
for each in buyers:
    a = each.strip()
    alist.append(a)
# print(alist)
adict = {}

xlist = [x.split(":") for x in alist]
# print(xlist)

for each in xlist:
    if len(each) > 1:
        # print(each[0]+":"+each[1])
        adict[each[0]] = each[1]
    else:
        adict[each[0]] = ""

# print(adict)
y = json.dumps(adict,indent=2)
print(y)


# with open("x.txt", "w", encoding="utf-8") as f:
#     f.write(x.text)