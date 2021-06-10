import face_recognition

input1 = input("First image")
input2 = input("Second image")

image1 = face_recognition.load_image_file(input1)
image2 = face_recognition.load_image_file(input2)

image1_encoding = face_recognition_encodings(image1)[0]
image2_encoding = face_recognition_encodings(image2)[0]

result = face_recognition.campare_faces([image1_encoding], image2_encoding)

if result[0]:
    print("Matched")

else
    print("Not matched")
