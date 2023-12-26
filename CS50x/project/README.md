# Mon-Kine
#### Video Demo:  <https://youtu.be/6-wkPMXF3xM>
#### Description:
Our web application is a platform for managing patient appointments and physiotherapy. It is built using PHP, a popular programming language for web development. The application includes several different features and functions to make it easy for patients to schedule appointments, for physiotherapists to manage their schedules and appointments, and for administrators to oversee the platform.

The main feature of our web application is the ability for patients to book appointments with physiotherapists. To make this process as simple as possible, we have included a user-friendly interface that allows patients to select from available dates and times that fit their schedule. Once an appointment is booked, patients can view and manage their appointments from their account, including the ability to cancel appointments if necessary.

For physiotherapists, we have included a feature that allows them to view and manage their schedules and appointments. They can see a calendar view of their schedule, and easily cancel an appointments as needed. They can also view details about their patients and their appointments, so they can be well-prepared for each session.

As an administrator, you have full control over the platform. You can view and manage the accounts of both patients and physiotherapists, as well as view and manage all appointments. You can also delete accounts or appointments as needed.

In addition to these core features, our web application also includes a contact form that allows users to send messages to the administrator. This is a convenient way for users to ask questions or provide feedback about the platform.

Our web application is composed of several different files, organized into separate folders for patients, physiotherapists, and administrators. Each folder contains the files needed to create the interface and functionality for that particular user group. We have also included a connection.php file, which handles the connection to the database when needed. Additionally, we have included a login.php file to handle user login and authentication, and a logout.php file to allow users to log out of their accounts.

Here are some examples of the specific files and their functions:

In the patient folder, the appointments.php file contains the appointment scheduling and management features for patients.
In the physiotherapist folder, the appointments.php file contains the features and functions for physiotherapists to view and manage their schedules and appointments.
In the admin folder, the appointments.php file contains the features and functions available to administrators for managing appointments, as well as the patient.php file, which contains features for managing accounts of patients and a kine.php which contains features for managing accounts of physio .
Overall, our web application is a valuable tool for anyone involved in the process of scheduling and managing appointments for physiotherapy. Whether you're a patient, a physiotherapist, or an administrator, our platform offers a simple and convenient way to manage appointments and stay organized.


#### How to upload the data base:
Here are the steps you can follow to upload a the database 'gestion_seances' to PHPMyAdmin using XAMPP, in order to use our web application 'Mon-Kine':

Start the Apache and MySQL modules in XAMPP. To do this, open the XAMPP Control Panel and click the "Start" button next to both "Apache" and "MySQL".

Open a web browser and go to the PHPMyAdmin login page by entering 
the URL 'http://localhost/phpmyadmin'

Log in to PHPMyAdmin using the username "root" and the password you set for the root user when installing XAMPP.

Once you are logged in, click the "Import" tab in the top menu.

Under "File to Import", click the "Choose File" button and select the 'gestion_seances.sql' database file. 

Click the "Go" button to start the import process. The progress of the import will be displayed on the screen.

When the import is complete, you should see a message indicating the number of queries that were executed successfully. You can then access the imported 'gestion_seances' database from the left menu under the "Databases" section.

Once the 'gestion_seances' database is uploaded and accessible in PHPMyAdmin,now you can use it with  our application 'Mon-Kine' .

I hope these steps help you successfully upload the 'gestion_seances' database to PHPMyAdmin using XAMPP, and use it with our 'Mon-Kine' web application. 

The administrator login is :
email:zaanouniab@gmail.com
password:123

