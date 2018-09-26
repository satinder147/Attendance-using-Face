# Face_recognition_attendance_system
# The Basic Approach
This is my attempt to make a Face recognition system for classroom or office attendance. The system is based on a special type of cnn architecture known as a siamese network. Such a network is trained to generate a very accurate and almost unique 128 vector given that the images of face which a are fed to the network are properly aligned and cropped. <br>
Then another dense neural network is trained taking input these embeddings. The second neural network is only for classification purposes. Then the person who is identified by the system, his/her attendance in the system is incremented by 1.<br>
When the system is closed, a excel file consisting of attendance of all the students is generated.

![maxresdefault](https://user-images.githubusercontent.com/24778913/46079121-d1ebd300-c1b3-11e8-88b7-ce9dba37b37e.jpg)
taken from DeepLearning.ai.<br>
You can watch these videos. Professor Andrew Ng gives an excellent explanation to these networks.

# Embedding Generator
I have download the pretrained facenet model from <a href="https://github.com/nyoki-mtl/keras-facenet"> nyoki-mtl githubu </a><br>
This network is pretrained on a pretty large dataset, and produces a unique 128 dimensional vector for a particular face given the images fed to it are cropped to only the face region and are alligned. The input size of image for this netowrk is 160X160X3

# Face Detection
Face detection is acheived by using haar cascades of opencv. Face detection haarcascade is used to detect the face and this detected region is fed to the embedding generator.


# The second neural net
The second neural network has a dense architecture and is used for classification. The second neural network take input the 128 dimensional vector and ouputs the probability of the face to be one of the student.The architecture of the second neural network is 
![screenshot from 2018-09-26 17-57-00](https://user-images.githubusercontent.com/24778913/46079781-b41f6d80-c1b5-11e8-9153-4716f6dcdc64.png)


# Updation of attendance
The database used is mongodb. Pymongo is used to add, delete records and also increment the attendance of the particular student.
![mongodb](https://user-images.githubusercontent.com/24778913/46079843-e7fa9300-c1b5-11e8-971b-413f9f304d49.png)


# csv file generation
After the application is closed, an excel file is generated. This excel file contains the attendance of all the student.

# Requiremnents
## Installing the requirements
1. Start your terminal of cmd depending on your os.
2. If you have a NVidia GPU then make sure you have the prerequisites for Tensorflow GPU installation (Refer to official site). Then use this commmand

    pip install -r requirements_gpu.txt

  3. In case you do not have a GPU then use this command

    pip install -r requirements_cpu.txt
   
 <br>
 Apart from all this you also have to install mongodb in your system.

# Want to run it on your own
1)Install all the requirements<br><br>
2)Make a folder named "people" without quotes<br><br>
3)Now run Generating_training_data.py, when this runs enter the name of the person followed by a index beginning from zero
for example, if I want to generate data for "ravi", I will write "ravi0" and for the next name write "secondname1", just make sure the index given to everybody is in increasing order. Now put all this folders into the people folder<br><br>
![screenshot from 2018-09-26 18-00-10](https://user-images.githubusercontent.com/24778913/46079905-16786e00-c1b6-11e8-9b20-47cd8c2c0edb.png)

4)Now in trainer.py change the number of classes according to number of folder and then run trainer.py<br><br>
5)The model will be trained.<br><br>
6)Now create a database using mongodb. Enter all the names with their attendance. This can be acheived by <br>
    a)create a data base named "new"<br>
    b)create a collection named "pa"<br>
    c)add the enteries. For eg db.pa.insert({"name":"satinder","attendance":0})<br><br>
    
  ![screenshot from 2018-09-26 18-02-31](https://user-images.githubusercontent.com/24778913/46080022-5f302700-c1b6-11e8-97a0-24df436396c0.png)

7)Now open recognizer.py and change the dictionary "a" and people according to your data. The key of array "a" is the index of the people and the data is a indicating variable which is used to indicate that in a particular session, if the person attendance has been taken.<br><br>
8)Dictionary "people" is self explanatory.<br><br>
9)Run recognizer.py to recognize people. Their attendance will be registered in the mongodb database. 

## Results
![screenshot from 2018-09-26 17-51-03](https://user-images.githubusercontent.com/24778913/46079517-f98f6b00-c1b4-11e8-83b6-206e028138a1.png)

## Updated attendance in the database
![screenshot from 2018-09-26 17-51-17](https://user-images.githubusercontent.com/24778913/46079581-26438280-c1b5-11e8-9fc5-70480e0e68b6.png)

## Liked it
If you liked it you will surely like my other repos as well. You can also have a look at my youtube channel <a href="https://www.youtube.com/c/reactorscience">"reactor science"</a>. If you have any doubts you can contact me on my facebook page <a href="https://www.facebook.com/pg/reactorscience/about/">"reactor science"</a>

## References
1)Deep learning with python by Francois Chollet<br>
2)keras.io<br>
3)Deeplearning.ai by coursera(prof Andrew Ng)<br>
4)CS231n by stanford<br>
5)Pyimagesearch.com(Adrian Rosenberg)<br>
6)Brandon Amos(github:https://github.com/bamos)
