from googleapiclient.discovery import build

# credentials
api_key = "AIzaSyCGZZL7o2nhpyZEaRs1c0NK_ArCS3tCWVk"
video_id = "zQDAi8tI-cU"

# build a resource for youtube
resource = build("youtube","v3",developerKey = api_key)

# create a request to get 20 comments on the video
# request = resource.commentThreads().list(
#     part="snippet",
#     videoId=video_id,
#     maxResults=1000,  # get 20 comments
#     order="orderUnspecified")  # top comments.

request = resource.commentThreads().list(
    part="snippet",
    videoId=video_id,
    maxResults = 1000
)
# execute the request
response = request.execute()

# get first 10 items for from 20 comments
items = response["items"]
print(items)
print("------------------------------------------------------------------------------------------------------")
# for item in items:

    # item_info = item["snippet"]
    #
    # # the top level comment can have sub reply comments
    # topLevelComment = item_info["topLevelComment"]
    # comment_info = topLevelComment["snippet"]
    #
    # print("Comment By:", comment_info["authorDisplayName"])
    # print("Coment Text:", comment_info["textDisplay"])
    # print("Likes on Comment :", comment_info["likeCount"])
    # print("Comment Date: ", comment_info['publishedAt'])
    # print("================================\n")