import requests

def Get3Words(coordinates):
    Words = {}
    API_KEY = 'UVTJLDJ2'
    r = requests.get('https://api.what3words.com/v3/convert-to-3wa?coordinates={0}%2C{1}&key={2}'.format(coordinates[0],coordinates[1],API_KEY))
    Response = r.json()['words'].split('.')

    for i in range(0, len(Response)):
        Words.update({'Word_' + str(i + 1): Response[i]})
    print(Words)
    return(Words)

def GetCoordinates(words):
    # In proccess
    Words = {}
    API_KEY = 'UVTJLDJ2'
    r = requests.get('https://api.what3words.com/v3/convert-to-coordinates?key={3}&words={0}.{1}.{2}&format=json'.format(words[0],words[1],words[2],API_KEY))
    Response = r.json()['square']
    Data = str(Response['northeast']['lat']) + ';' + str(Response['southwest']['lat']) + ';' + str(Response['northeast']['lng']) + ';' + str(Response['southwest']['lng'])
    return Data
if __name__ == '__main__':
    word1, word2, word3 = input().split()
    GetCoordinates((word1, word2, word3))
