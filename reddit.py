import praw
import datetime
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import urllib.request, io, base64, tkinter

# r = praw.Reddit(user_agent='my_cool_application')
# submissions = r.get_subreddit('opensource').get_hot(limit=5)
# [str(x) for x in submissions]
#

class rpie_reddit:
    def __init__(self):
        self.r = praw.Reddit(client_id='RueX_EgGGUBJmA',
                        client_secret='4RnyFCr9BpH0UN4JdoJ-Xm0Tg-k',
                        password='reddit56',
                        user_agent='/u/kwar1313',
                        username='kwar1313',
                        redirect_uri='http://localhost:8080'
                        )

        self.n_length_hot = 100

        print(self.r.auth.url(['identity'], '...', 'permanent'))

    def get_dadjoke(self):
        hot_posts = list(self.r.subreddit('dadjokes').hot(limit=self.n_length_hot))

        nrand = random.randrange(self.n_length_hot)

        return hot_posts[nrand].title, hot_posts[nrand].selftext


    def get_smol_cat(self):
        hot_posts = list(self.r.subreddit('IllegallySmolCats').hot(limit=self.n_length_hot))

        while True:
            nrand = random.randrange(self.n_length_hot)
            if '.jpg' in hot_posts[nrand].url or '.gif' in hot_posts[nrand].url:
                break
                # return hot_posts[nrand].url

        path = io.BytesIO(urllib.request.urlopen(hot_posts[nrand].url).read())
        # Image.open(path).show()

        ImageAddress = path
        ImageItself = Image.open(ImageAddress)
        ImageNumpyFormat = np.asarray(ImageItself)
        plt.imshow(ImageNumpyFormat)
        plt.draw()
        plt.pause(7) # pause how many seconds
        plt.close()

        return hot_posts[nrand]



if __name__ == '__main__':
    r = rpie_reddit()

    _ = r.get_smol_cat()

    print(r.get_dadjoke())
    print(f'{datetime.datetime.now()} | Done.')

