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
    '❤': 3,
    '😢': 1,
    '💔': 1,
    '❤🔥': 3,
    '💩': -2,
    '🙏': 1,
    '👍': 2,
    '⚡': 2,
    '🔥': 2,
    '🥰': 3,
    '🤯': 1,
    '🐳': -1,
    '🏆': 2,
    '😁': 2,
    '🎉': 2,
    '🤩': 2,
    '😍': 1,
    '🤮': -3,
    '😱': -1,
    '👏': 1,
    '🤡': -1,
    '💯': 2,
    '🕊': 2,
    '🤔': -1,
    '🍌': -1,
    '👎': -2,
    '🤨': -1,
    '🤬': -2,
    '🤣': 2,
    '🌭': 1,
    '😐': -1,
    '🥴': -1,
    '🌚': -2,
    '🥱': -1
}


# def read_reactions():
#     emoji = ['❤', '😢', '💔', '❤🔥', '💩', '🙏', '👍', '⚡', '🔥', '🥰', '🤯', '🐳', '🏆', '😁', '🎉', '🤩', '😍', '🤮', '😱', '👏', '🤡', '💯', '🕊', '🤔', '🍌', '👎', '🤨', '🤬', '🤣', '🌭', '😐', '🥴', '🌚', '🥱']
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
