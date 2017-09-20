**Python test**

**Steps to run the application**

**Virtual Environment :**  Create virtual environment using command *virtualenv python_test_env*

**Activate Environment :** activate the virtual environment *source python_test_env/bin/activate*

**Requirements.** install the requirements in virtual env using *pip install -r requirements.txt*

**Make Migrations** *python manage.py makemigrations*

**Migrate** *python manage.py migrate*

**Load Dummy Data** Load dummy data using *python manage.py loaddata fixtures/data.json*

**Run the Server** *python manage.py runserver*

**Demo accounts**

* username - user_1, password - userpass1
* username - user_2, password - userpass2
* username - user_3, password - userpass3
* username - user_4, password - userpass4


* tanant - neosoft  api-key - 23cb00a63d7945eba0ff5b846de1b728
* tenant - webwerks api-key - 3c1a5d88ac914da6a92e860789453779

**apis**

* get access token
     * url - <Domain Name>/api-token-auth/
     * method - POST
     * params - username, password

* get questions
    * url - <Domain Name>/apis/questions
    * method - GET
    * headers - token, api-key
    * params - q (optional)
