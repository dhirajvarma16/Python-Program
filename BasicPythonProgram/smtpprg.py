import urllib2

proxy_support = urllib2.ProxyHandler({"http":"http://61.233.25.166:80"})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)

html = urllib2.urlopen("http://www.google.com").read()
print html