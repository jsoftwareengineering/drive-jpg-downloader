import urllib

counter = 0
fileID = ''
with open('links.txt') as f:
	for line in f:
		if len(line) < 70:
			stri = line.split('id=')
			stri = stri[1].split('\n')
			print(str(counter) + ' ' + stri[0])
			fileID = stri[0]

		else:
			stri = line.split('/d/')
			stri = stri[1].split('view')
			stri = stri[0].split('/')
			print(str(counter) + ' ' + stri[0])
			fileID = stri[0]

		link = 'http://drive.google.com/uc?export=download&id=' + fileID
		path = 'photos/' + str(counter) + '.jpg'
		
		print(link)
		print(path)
		
		urllib.urlretrieve(link, path)
		counter = counter + 1



