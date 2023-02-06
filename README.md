## My own social network on Django and Websockets



## If you want to change  settings, you should edit the env file



Launch
------

```
git clone https://github.com/BenitoSwaggolini/Social_Network.git
python -m venv venv
.\venv\Scripts\activate
cd Social_Network
pip install Django==3.2.6
pip install -U channels["daphne"]
pip install -r requirements.txt
cd src
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```



Docker
------

```
git clone https://github.com/BenitoSwaggolini/Website-for-calculating-expenses.git
docker-compose up -d
```




Opportunities(over time, there will be more of them):
------


* Online dynamic chats
* News
* Friendship system(friendship requests + delete/add)
* User profile and posts
* User infinite scroll
* Notifications