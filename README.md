# edfox1

Fork , clone and setup project in your local computer

Open a new terminal and type the command:
ssh ubuntu@ec2-3-14-81-136.us-east-2.compute.amazonaws.com

Required Key Pair for this instance is available at AWS account Key pairs.

After connecting to AWS through terminal type the commands:
ls       
output: edfox1   env

source env/bin/activate
cd edfox1

git remote -v 
output: https://github.com/Anu-123-gif/edfox1
*You can change the remote repository and set it to your own*

git pull    (To get any changes made on the repository onto the AWS instance)

cd django_school

gunicorn --bind 0.0.0.0:8000 django_school.wsgi:application
This will activate the instance which will now be accessible through link:  
http://ec2-3-14-81-136.us-east-2.compute.amazonaws.com:8000/


Cheers!
 
