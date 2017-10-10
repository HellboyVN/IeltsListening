import urllib

for num in range(12,35):
    testfile = urllib.URLopener()
    testfile.retrieve("https://raw.githubusercontent.com/ryanle-gamo/english-listening-data/master/basic_lession"+str(num)+".mp3", "basic_lession"+str(num)+".mp3")
print 'done'
