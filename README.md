## Identifier :

#### Problem Statement : Verification of the name and face of an individual using his or her Pan Card.

              In this prototype, the Pan Card belong to a particular individual 
              and for its use cases, it is advised to replace that pan card in the 
              file section from the new one for testing with the same file name.
              
              * supported file format is -> .jpeg
              
 
 
 ### Steps to be followed :
 
 - Installation of all the packages : (Make sure all the packages are properly installed in the device for smooth functioning of application)
              
              TensorFlow
              Keras
              Keras-VGG Face
              MTCNN model
              Tessaract 
              Pytessaract
              Pandas
              CV2
              Flask

- Download the code file/clone the repository.
- Open your terminal/command line 
- Reach out to the directory where the model is being downloaded/cloned
- In the terminal type : "python app.py"
- It will run and we will be provided with a local host link refering to local host :5000 (in most cases)
- Follow up the link.
- Fill in the details as asked in the webpage and then your name would be validate with the one shared by you and in the pan card.
- Then move to the top of the browser wherein the link is pasted and then type "/video_feed" after 5000 in order to do the face verification.
- If the face matches with the one in Pan Card, you will receive a message of verified with your picture taken from the webcam.
              

