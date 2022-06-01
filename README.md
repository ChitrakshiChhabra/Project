## Identifier :

#### Problem Statement : Verification of the name and face of an individual using his or her Pan Card.

              In this prototype, the Pan Card belong to a particular individual 
              and for its use cases, it is advised to replace that pan card in the 
              file section from the new one and also update its path for testing 
              with proper file address and name.
              
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
- Follow up the link and you will be able to see a web app like given below.

- <img width="1792" alt="Screenshot 2022-06-01 at 8 32 54 AM" src="https://user-images.githubusercontent.com/73769058/171319984-6ba802ae-9910-4bd0-86ac-056690400f33.png">

- Fill in the details as asked in the webpage and then your name would be validate with the one shared by you and in the pan card.

- <img width="1792" alt="Screenshot 2022-06-01 at 8 33 14 AM" src="https://user-images.githubusercontent.com/73769058/171320081-c5bd1875-efe8-4cd0-b42e-8630f6f55784.png">

- <img width="1792" alt="Screenshot 2022-06-01 at 8 33 31 AM" src="https://user-images.githubusercontent.com/73769058/171320215-839db2a6-9762-4486-b914-2a2bc7dce3f7.png">


- Then move to the top of the browser wherein the link is pasted and then type "/video_feed" after 5000 in order to do the face verification.

- <img width="1792" alt="Screenshot 2022-06-01 at 8 34 03 AM" src="https://user-images.githubusercontent.com/73769058/171320265-da399bdd-86fb-4881-93f0-ce220624a60e.png">


- If the face matches with the one in Pan Card, you will receive a message of verified with your picture taken from the webcam.

- <img width="1792" alt="Screenshot 2022-06-01 at 8 34 23 AM" src="https://user-images.githubusercontent.com/73769058/171320301-117adc15-4729-439e-aabb-6b443a21d541.png">
