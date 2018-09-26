# Face_recognition_attendance_system
# The Basic Approach
This is my attempt to make a Face recognition system for classroom or office attendance. The system is based on a special type of cnn architecture known as a siamese network. Such a network is trained to generate a very accurate and almost unique 128 vector given that the images of face which a are fed to the network are properly aligned and cropped. <br>
Then another dense neural network is trained taking input these embeddings. The second neural network is only for classification purposes. Then the person who is identified by the system, his/her attendance in the system is incremented by 1.<br>
When the system is closed, a excel file consisting of attendance of all the students is generated.

# Embedding Generator
I have download the pretrained facenet model from <a href="https://github.com/nyoki-mtl/keras-facenet"> nyoki-mtl githubu </a><br>
This network is pretrained on a pretty large dataset, and produces a unique 128 dimensional vector for a particular face given the images fed to it are cropped to only the face region and are alligned. The input size of image for this netowrk is 160X160X3

# Face Detection
Face detection is acheived by using haar cascades of opencv. Face detection haarcascade is used to detect the face and this detected region is fed to the embedding generator.

# The second neural net
The second neural network has a dense architecture and is used for classification. The second neural network take input the 128 dimensional vector and ouputs the probability of the face to be one of the student.The architecture of the second neural network is 

# Updation of attendance
The database used is mongodb. Pymongo is used to add, delete records and also increment the attendance of the particular student.

# csv file generation
After the application is closed, an excel file is generated. This excel file contains the attendance of all the student.

