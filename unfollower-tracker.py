import json

with open('followers_and_following/following.json') as file:
    following_json = json.load(file)

with open('followers_and_following/followers.json') as file:
    followers_json = json.load(file)

with open('whitelist.json') as file:
    whitelist_json = json.load(file)

following_list = []
for following in following_json["relationships_following"]:
    following_list.append(following["string_list_data"][0]["value"])

followers_list = []
for follower in followers_json["relationships_followers"]:
    followers_list.append(follower["string_list_data"][0]["value"])

not_following_back_list = list(set(following_list) - set(followers_list) - set(whitelist_json))

print(f'These people are not following you back on Instagram ({len(not_following_back_list)}):')
for user in not_following_back_list:
    print(f'{user} (https://instagram.com/{user})')
