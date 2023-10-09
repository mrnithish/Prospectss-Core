from youtube_transcript_api import YouTubeTranscriptApi
import os
videoLink='https://www.youtube.com/watch?v=uYPbbksJxIg' ## video link
video_id=videoLink.split('=')[1]

# print(video_id)

outls = []
#clear the text file
with open("op.txt",'w') as file:
        pass
try:
     
    tx = YouTubeTranscriptApi.get_transcript(video_id,languages=['en'])
    for i in tx:
        outtxt=(i['text'])
        outls.append(outtxt)
        with open("op.txt", "a") as opf:
            opf.write(outtxt + "\n")
    print("Successfull")
except Exception as e:
    print("No subtitle")

# from sklearn. feature_extraction.text import CountVectorizer
# # Create a Vectorizer Object
# vectorizer = CountVectorizer()
# vectorizer.fit(outls)
# # Printing the identified Unique words along with their indices
# print("Vocabulary: ", vectorizer.vocabulary_)


#other logic
#vid_id = 'y0oWA2yVB3s'
# #extract text
# data = yta.get_transcript (vid_id)
# #Step 3 : our logic to make transcript more better
# transcript =''
# for value in data:
#   for key, val in value.items():
#       if key == 'text':
#           transcript += val
# l = transcript.splitlines ()
# final tra = ' '.join (l)
# #Step 4 : Write out transcript in the file
# file = open("Guruji.txt",'w')
# file.write(final_tra)
#file.close()