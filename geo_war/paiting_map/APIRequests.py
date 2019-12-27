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
    print(r.json()['square'])

if __name__ == '__main__':
    Get3Words((51.521251, -0.203586))
