import matplotlib
matplotlib.use('Agg')
import datetime
from imgurpython import ImgurClient

client_id = 'fc280e832eb18a5'
client_secret = '8088de037da2f04030c98d44659fe28026a17c72'
album_id = 'O5w6BiM'
access_token = '930e5d2ec31c2451120265157802b05592e788da'
refresh_token = '2dff55f14878494b83e87935b18af4955624038c'

def showImgur(fileName):
    client = ImgurClient(client_id, client_secret, access_token, refresh_token)

    config = {
        'album': album_id,
        'name': fileName,
        'title': fileName,
        'description': str(datetime.date.today())
    }

    try:
        print("[log:INFO]Uploading image... ")
        imgurl = client.upload_from_path(fileName+'.png', config=config, anon=False)['link']
        print("[log:INFO]Done upload. ")
    except:
        imgurl = 'https://i.imgur.com/RFmkvQX.jpg'
        print("[log:ERROR]Unable upload ! ")

    return imgurl