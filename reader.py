import json
import time

# a = {"_": "Message", "id": 316, "peer_id": {"_": "PeerChannel", "channel_id": 1315916212}, "date": "2022-09-06T13:02"
#                                                                                                    ":49+00:00",
#      "message": "сегодня стрим по хоррору Гост Вотчерс супер жёстким стаком w/ avalanche99, Daeryyn, "
#                 "ajaoffski \nПримерно в 17:30-18:00 мск \nМне уже страшно, всех жду епт 😘", "out": false,
#      "mentioned": false, "media_unread": false, "silent": false, "post": true, "from_scheduled": false,
#      "legacy": false, "edit_hide": true, "pinned": false, "noforwards": false, "from_id": null, "fwd_from": null,
#      "via_bot_id": null, "reply_to": null, "media": null, "reply_markup": null, "entities": [], "views": 39,
#      "forwards": 0, "replies": {"_": "MessageReplies", "replies": 1, "replies_pts": 1151, "comments": true,
#                                 "recent_repliers": [{"_": "PeerUser", "user_id": 2007095935}], "channel_id":
#                                     1766910827, "max_id": 724, "read_max_id": null}, "edit_date":
#          "2022-09-06T13:16:23+00:00", "post_author": null, "grouped_id": null, "reactions": {"_": "MessageReactions",
#                                                                                              "results": [{"_":
#                                                                                                               "ReactionCount",
#                                                                                                           "reaction": "🔥",
#                                                                                                           "count": 3,
#                                                                                                           "chosen": false}],
#                                                                                              "min": false,
#                                                                                              "can_see_list": false,
#                                                                                              "recent_reactions": []},
#      "restriction_reason": [], "ttl_period": null}

c = []
with open("channel_messages.json", "r") as f:
    file = json.loads(f.read())
n = len(file)
count = 0
q = time.time()
for i in range(0, n // 20):
    k = file[i].keys()
    if 'reactions' in k:
        k2 = file[i].keys()
        if file[i]['reactions']:
            for reaction in file[i]['reactions']['results']:
                count += reaction['count']

z = n // 20
z = count // z
print(z)
count3=0
for i in range(0, n // 11):
    k = file[i].keys()
    if 'reactions' in k:
        k2 = file[i].keys()
        if file[i]['reactions']:
            count2 = 0
            for reaction in file[i]['reactions']['results']:
                count2 += reaction['count']
            if count2 > z:
                print('https://t.me/SilverNameTV/'+str(file[i]['id']))
                count3 += 1
print(count3)

