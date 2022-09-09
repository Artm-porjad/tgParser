import json
import time

# a = {"_": "Message", "id": 316, "peer_id": {"_": "PeerChannel", "channel_id": 1315916212},
# "date": "2022-09-06T13:02" ":49+00:00", "message": "сегодня стрим по хоррору Гост Вотчерс супер жёстким стаком w/
# avalanche99, Daeryyn, " "ajaoffski \nПримерно в 17:30-18:00 мск \nМне уже страшно, всех жду епт 😘", "out": false,
# "mentioned": false, "media_unread": false, "silent": false, "post": true, "from_scheduled": false, "legacy": false,
# "edit_hide": true, "pinned": false, "noforwards": false, "from_id": null, "fwd_from": null, "via_bot_id": null,
# "reply_to": null, "media": null, "reply_markup": null, "entities": [], "views": 39, "forwards": 0, "replies": {"_":
# "MessageReplies", "replies": 1, "replies_pts": 1151, "comments": true, "recent_repliers": [{"_": "PeerUser",
# "user_id": 2007095935}], "channel_id": 1766910827, "max_id": 724, "read_max_id": null}, "edit_date":
# "2022-09-06T13:16:23+00:00", "post_author": null, "grouped_id": null, "reactions": {"_": "MessageReactions",
# "results": [{"_": "ReactionCount", "reaction": "🔥", "count": 3, "chosen": false}], "min": false, "can_see_list":
# false, "recent_reactions": []}, "restriction_reason": [], "ttl_period": null}

c = []
with open("channel_messages.json", "r") as f:
    file = json.loads(f.read())

len_posts = len(file)
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
#
#     return emoji
#
#
# print(read_reactions())


def posts_reaction():
    count = 0
    for i in range(0, n):
        k = file[i].keys()
        if 'reactions' in k:
            if file[i]['reactions']:
                for reaction in file[i]['reactions']['results']:
                    count += reaction['count'] * emojo_rating[reaction['reaction']]
    print(count, n)
    print(count // n)
    return count // n


sr_rait = posts_reaction()


count3 = 0
for i in range(0, n):
    k = file[i].keys()
    if 'reactions' in k:
        if file[i]['reactions']:
            count2 = 0
            for reaction in file[i]['reactions']['results']:
                count2 += reaction['count'] * emojo_rating[reaction['reaction']]
            if count2 > sr_rait:
                print('https://t.me/Cbpub/' + str(file[i]['id']))
                count3+=1
print(count3)
