import indicoio
from indicoio.custom import Collection
# from PIL import Image
# import numpy as np

indicoio.config.api_key = '7a8f16edc7a58c8a7773ba95c6d2241b'

collection2 = Collection("collection_name")

h1 = indicoio.fer("https://upload.wikimedia.org/wikipedia/commons/2/27/Hillary_Clinton_official_Secretary_of_State_portrait_crop.jpg")
t1 = indicoio.fer("http://i2.cdn.turner.com/money/dam/assets/160224112545-trump-nevada-victory-speech-780x439.jpg")
# Add Data
# collection.add_data([["indico is so easy", "label1"], ["text2", "label2"]])
collection2.add_data([["https://upload.wikimedia.org/wikipedia/commons/2/27/Hillary_Clinton_official_Secretary_of_State_portrait_crop.jpg", "hillary"], ["http://i2.cdn.turner.com/money/dam/assets/160224112545-trump-nevada-victory-speech-780x439.jpg", "trump"]])

# Training
collection2.train()

# Telling Collection to block until ready
collection2.wait()

# Done! Start analyzing text
print collection2.predict("indico is so easy to use!")