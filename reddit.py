import praw
import datetime
import random

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

if __name__ == '__main__':
    r = rpie_reddit()

    print(r.get_dadjoke())
    print(f'{datetime.datetime.now()} | Done.')

