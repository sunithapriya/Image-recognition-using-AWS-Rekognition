import boto3, requests
session = boto3.Session(profile_name='sunithap')
rekognition = session.client('rekognition')

#Detect faces
response = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Stephen_Hawking_David_Fleming_Martin_Curley.png/640px-Stephen_Hawking_David_Fleming_Martin_Curley.png')
response_content = response.content

#Detect Celebrities
rekognition_response = rekognition.detect_faces(Image={'Bytes': response_content}, Attributes=['ALL'])
#print(rekognition_response)

rekognition_celeb_response = rekognition.recognize_celebrities(Image={'Bytes': response_content})
print(rekognition_celeb_response)

#Face Match
source_response = requests.get('https://cdn.thinglink.me/api/image/515911285833990144/1240/10/scaletowidth')
source_response_content = source_response.content
target_response = requests.get('http://i.telegraph.co.uk/multimedia/archive/02648/Hawking_2648775k.jpg')
target_response_content = target_response.content
rekognition_response = rekognition.compare_faces(SourceImage={'Bytes': source_response_content}, TargetImage={'Bytes': target_response_content}, SimilarityThreshold=70 ) 
 
for face_match in rekognition_response['FaceMatches']:
        position = face_match['Face']['BoundingBox']
        confidence = str(face_match['Face']['Confidence'])
        print('The face at ' +
               str(position['Left']) + ' ' +
               str(position['Top']) +
               ' matches with ' + confidence + '% confidence')