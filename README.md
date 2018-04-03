**Python Flask Application with Apache and WSGI Setup**  

**Application**  

The application deployed takes the user input and tells us if it is a Pangram or not a pangram.

A pangram is a sentence or any word having all the alphabets (A-Z).

Success Case:
Input: The quick brown fox jumps over the lazy dog
Output: Yayy!!! The entered sentence is a pangram.

Failure Case:
Input: Anything which doesnt have all the alphabets
Output: Oops!!! The entered sentence is not a pangram.

Used Technologies: HTML, CSS for Styling, Python 2.7, Flask

Used GET and POST method for the form to get user input and post the result.

Python has been setup with wsgi server with host being apache2 server. Please find the steps to deploy Flask Application under Apache WSGI in Amazon Linux AMI. Please add 'sudo' command if in case you get any permission errors.

Install apache by using below reference:
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-LAMP.html

**Installation/Using WSGI:**  

1. Install flask
pip install flask

2. Installing wsgi module
install mod24_wsgi-python27.x86_64

3. Installing Virtual Environment
pip install virtualenv 
virtualenv venv

4. To activate venv
source venv/bin/activate 

5. Please follow the mentioned folder structure: In my case it is as below:
------/var/www  
--------------/Pangram  
-----------------------/pangram.wsgi  
-----------------------/Pangram  
-------------------------------/__init__.py  
-------------------------------/static  
-----------------------------------------/styles.css  
-------------------------------/templates  
-----------------------------------------/ispangram.html  
-----------------------------------------/pangram.html  
-----------------------------------------/notpangram.html  
-------------------------------/venv  

6. To check if the app is working, run below command and check if you get "Running on http://localhost:5000/"
python __init__.py 

7. Prepare WSGI file by using below code:

#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/Pangram/")

from Pangram import app as application
application.secret_key = 'your secret key'

8. Configure you application configuration file by using VI editor by below command and paste the necessary content shown.
vi /etc/httpd/conf.d/Pangram.conf

**Content:** 
<VirtualHost *:80>
    WSGIScriptAlias / /var/www/Pangram/pangram.wsgi
    <Directory /var/www/Pangram/Pangram/>
        Order allow,deny
        Allow from all
    </Directory>
    Alias /static /var/www/Pangram/Pangram/static
   <Directory /var/www/Pangram/Pangram/static/>
        Order allow,deny
        Allow from all
   </Directory>
</VirtualHost>

9. Now restart apache
sudo service httpd restart

**References:**  
https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
https://www.jakowicz.com/flask-apache-wsgi/
http://peatiscoding.me/geek-stuff/mod_wsgi-apache-virtualenv/


**Configuring Self Signed SSL Certificate to bring HTTPS: **  
1. Installation of required modules like mod_ssl
2. Generation of a key and certificate.
3. Modifying configuration files such as Pangram.conf, httpd.conf, ssl.conf

**References:** 
https://www.digitalocean.com/community/tutorials/how-to-create-an-ssl-certificate-on-apache-for-centos-7
https://www.digicert.com/csr-ssl-installation/apache-openssl.htm
