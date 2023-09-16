import json

following_json_file = "following.json"
followers_json_file = "followers_1.json"

# フォローを読み込む
with open(following_json_file, 'r', encoding='utf-8') as following_json:
    following_data = json.load(following_json)
following_id = set(entry["string_list_data"][0]["value"] for entry in following_data["relationships_following"])

# フォロワーを読み込む
with open(followers_json_file, 'r', encoding='utf-8') as followers_json:
    followers_data = json.load(followers_json)
followers_id = set(entry["string_list_data"][0]["value"] for entry in followers_data)

# 比較
follow_only =  following_id - followers_id #片思いしてる
follower_only = followers_id - following_id #片思いされている
follow_and_follower = following_id.intersection(followers_id) #両想い

# 出力
print("\n######あなたが一方的にフォローしている人######")
for id_follow in follow_only:
    print(f"{id_follow}")
print(f"\n######あなたを一方的にフォローしている人######")
for id_follower in follower_only:
    print(f"{id_follower}")
print(f"\n######相互フォローしている人######")
for id_follow_and_follower in follow_and_follower:
    print(f"{id_follow_and_follower}")