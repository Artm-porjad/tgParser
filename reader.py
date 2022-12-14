import json
import time

c = []
with open("channel_messages.json", "r") as f:
    file = json.loads(f.read())

len_posts = len(file)
print(len_posts)
n = len_posts // 20
q = time.time()

emojo_rating = {
    'โค': 3,
    '๐ข': 1,
    '๐': 1,
    'โค๐ฅ': 3,
    '๐ฉ': -2,
    '๐': 1,
    '๐': 2,
    'โก': 2,
    '๐ฅ': 2,
    '๐ฅฐ': 3,
    '๐คฏ': 1,
    '๐ณ': -1,
    '๐': 2,
    '๐': 2,
    '๐': 2,
    '๐คฉ': 2,
    '๐': 1,
    '๐คฎ': -3,
    '๐ฑ': -1,
    '๐': 1,
    '๐คก': -1,
    '๐ฏ': 2,
    '๐': 2,
    '๐ค': -1,
    '๐': -1,
    '๐': -2,
    '๐คจ': -1,
    '๐คฌ': -2,
    '๐คฃ': 2,
    '๐ญ': 1,
    '๐': -1,
    '๐ฅด': -1,
    '๐': -2,
    '๐ฅฑ': -1
}


# def read_reactions():
#     emoji = ['โค', '๐ข', '๐', 'โค๐ฅ', '๐ฉ', '๐', '๐', 'โก', '๐ฅ', '๐ฅฐ', '๐คฏ', '๐ณ', '๐', '๐', '๐', '๐คฉ', '๐', '๐คฎ', '๐ฑ', '๐', '๐คก', '๐ฏ', '๐', '๐ค', '๐', '๐', '๐คจ', '๐คฌ', '๐คฃ', '๐ญ', '๐', '๐ฅด', '๐', '๐ฅฑ']
#     for i in range(0, n // 20):
#         k = file[i].keys()
#         if 'reactions' in k:
#             if file[i]['reactions']:
#                 for reaction in file[i]['reactions']['results']:
#                     if not reaction['reaction'] in emoji:
#                         emoji.append(str(reaction['reaction']))
#     return emoji

# print(read_reactions())


def posts_reaction():
    count_reactions = 0
    count_views = 0
    for i in range(0, n):
        k = file[i].keys()
        if file[i]['_'] != 'MessageService':
            if 'reactions' in k:
                if file[i]['reactions']:
                    for reaction in file[i]['reactions']['results']:
                        count_reactions += reaction['count'] * emojo_rating[reaction['reaction']]

            if 'views' in k:
                if file[i]['views']:
                    count_views += file[i]['views']

    print(n)
    print(count_views // n)
    print(count_reactions // n)
    return count_views // n, count_reactions // n


sr_views, sr_react = posts_reaction()

count3 = 0
for i in range(0, n):
    count_emoji = 0
    count_views = 0
    k = file[i].keys()
    if file[i]['_'] != 'MessageService':
        if 'reactions' in k:
            if file[i]['reactions']:
                for reaction in file[i]['reactions']['results']:
                    count_emoji += reaction['count'] * emojo_rating[reaction['reaction']]
            if file[i]['views']:
                count_views += file[i]['views']
                if count_views >= sr_views and count_emoji >= sr_react:
                    print('https://t.me/rian_ru/' + str(file[i]['id']))
                    count3 += 1
        else:
            if file[i]['views']:
                count_views += file[i]['views']
                if count_views >= sr_views:
                    print('https://t.me/rian_ru/' + str(file[i]['id']))
                    count3 += 1

print(count3, n)
