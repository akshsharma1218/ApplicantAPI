# ApplicantAPI
A rest app for a Job application review system. 
It have api endpoints to create, retrieve, update, delete and list the information of an applicant.
It also have a feature to mark applicants Selected or rejected.
It also have the functionality to upload resumes of the applicant along with rest of the info.
It also have filtering and pagination in the applicant listing api.


# Set Up
1. Clone repo using : ` git clone https://github.com/akshsharma1218/ApplicantAPI`
2. Create virtual enviroment : `python3 -m venv env`   &emsp;&emsp;&emsp; # for linux
3. Change directory : `cd rest_app`
4. Install requirements : `pip install -r requirements.txt`
5. Run migrations : `python3 manage.py makemigrations`</br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;`python3 manage.py migrate`
6. Run server : `python3 manage.py runserver`

# Routes :

Home page or list page : `http://127.0.0.1:8000/` </br></br>
Particular applicant retrive/update/delete : `http://127.0.0.1:8000/<id>`  &emsp;&emsp;&emsp; # eg : `http://127.0.0.1:8000/1`

# Preview
## Applicant List View with pagignation
![Applicant List View witg pagignation](rest_app/preview/list.png)
## Filtering
![Filtering](rest_app/preview/Filtering.png)
## Applicant Create View
![Applicant Create View](rest_app/preview/Create.png)
## Applicant Created Response
![Applicant Created Response](rest_app/preview/created.png)
## Applicant Update Delete View
![Applicant Update Delete View](rest_app/preview/update-delete.png)

