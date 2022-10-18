# from googleapiclient.discovery import build
# import pandas
#
# api_key = "AIzaSyCGZZL7o2nhpyZEaRs1c0NK_ArCS3tCWVk"
# video_ID = "zQDAi8tI-cU"
#
# fetch = build("youtube","v3",developerKey = api_key)
# req = fetch.commentThreads().list(
#     part = "snippet",
#     videoId = video_ID,
#     maxResults = 1000
# )
#
# response = req.execute()
# item = response["items"]
# print("------------------------------------------------------------------------------------------------------")
# Comment = []
# CommentorName =[]
# Likes = []
# for a in item:
#     Comment.append(a["snippet"]["topLevelComment"]["snippet"]["textDisplay"])
#     CommentorName.append(a["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"])
#     Likes.append(a["snippet"]["topLevelComment"]["snippet"]["likeCount"])
#
# Data = {
#     "Comment": Comment,
#     "CommentName" : CommentorName,
#     "Likes": Likes
# }
#
# a = pandas.DataFrame(Data)
# a.to_csv("YoutubeComment.csv",index=False,encoding="utf-8")
# print(a)


#from googleapiclient.discovery import build
from googleapiclient.discovery import build

api_key = 'AIzaSyCGZZL7o2nhpyZEaRs1c0NK_ArCS3tCWVk'
video_id = "CxcRDfizYzY"


	# empty list for storing reply
replies = []

	# creating youtube resource object
youtube = build('youtube', 'v3',
					developerKey=api_key)

	# retrieve youtube video results
video_response=youtube.commentThreads().list(
	part='snippet,replies',
	videoId=video_id
	).execute()

	# iterate video response
while video_response:

		# extracting required info
		# from each result object
	for item in video_response['items']:

			# Extracting comments
		comment = item['snippet']['topLevelComment']['snippet']['textDisplay']

			# counting number of reply of comment
		replycount = item['snippet']['totalReplyCount']

			# if reply is there
		if replycount>0:

				# iterate through all reply
			for reply in item['replies']['comments']:

					# Extract reply
				reply = reply['snippet']['textDisplay']

					# Store reply is list
				replies.append(reply)

			# print comment with list of reply
		print(comment, replies, end = '\n\n')

			# empty reply list
		replies = []

		# Again repeat
	if 'nextPageToken' in video_response:
		video_response = youtube.commentThreads().list(
					part = 'snippet,replies',
					videoId = video_id
				).execute()
	else:
		break

# Enter video id


