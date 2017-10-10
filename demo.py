import urllib

for num in range(1,35):
    testfile = urllib.URLopener()
    testfile.retrieve("https://raw.githubusercontent.com/ryanle-gamo/english-listening-data/master/intermediate_lession"+str(num)+".mp3", "intermediate_lession"+str(num)+".mp3")
print 'done'
