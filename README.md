To run the project, first clone the repository or download and extract the zip file and install the required packages and dependencies using the command
> pip install -r requirements.txt

To run the Django project, execute the following command
> python manage.py runserver

If there is some new user that wants to use our online platform for booking a bus ticket then he has to register into the system to use the various functionalities provided by the system.In order to sign up/register for the usage of this platform every user has to provide some mandatory information like email address , date of birth , address , pincode , mobile number , password and on clicking register button,welcome message will be sent on their mail and now they can use the various functionalities of the system.

![Alt text](screenshots/register.png?raw=true "Register")



Once the user registers into the system then he/she needs to login to the system to use the functionalities 

![Alt text](screenshots/login.png?raw=true "Login")



On logging into the system,admin can view buses, add new buses, update bus info, make buses unavailable.

![Alt text](screenshots/admin_crud.png?raw=true "Admin CRUD")



The customer can select the bus through filtered search and select the seat through simulation UI.

![Alt text](screenshots/seat_book.png?raw=true "Seat Selection")



The history of all the bookings done by customer is visible to the customer for his/her reference.

![Alt text](screenshots/my_bookings.png?raw=true "Bookings History")

