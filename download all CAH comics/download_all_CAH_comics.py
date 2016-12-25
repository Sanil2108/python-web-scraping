import bs4, requests, urllib
def getAndSaveComics(amount, local_path='', start=4500):
    str_='http://explosm.net/comics/'
    if start==4500:
        start=4500-amount
    for i in range(start, 4500, 1):
        str_updated=str_+str(i)
        getAndSaveComic(str_updated, i, local_path)


def getAndSaveComic(url_path, j, local_path=''):
    # First initialize the list that will hold all img source
    list_of_imgs = []
    soup = bs4.BeautifulSoup(requests.get(url_path).text, 'html5lib')
    all_imgs = soup.find_all('img')
    for i in range(len(all_imgs)):
        if 'id' in all_imgs[i].attrs.keys():
            if all_imgs[i].attrs['id'] == 'main-comic':
                list_of_imgs.append(all_imgs[i].attrs['src'])

    print('started for ', list_of_imgs, end='\t')

    try:
        if(local_path is not ''):
            urllib.request.urlretrieve('http:' + list_of_imgs[0], local_path + '/' + str(j) + '.png')
        else:
            urllib.request.urlretrieve('http:' + list_of_imgs[0], str(j) + '.png')
    except Exception as e:
        print('\nSomething went wrong at image number', j)
        return

    print('\t\t\tDONE !!')

getAndSaveComics(100)