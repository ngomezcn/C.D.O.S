#### Deploy
- Clone repo ```git clone https://github.com/ngomezcn/C.D.O.S```
- Create venv on root ```python -m venv venv```
- Activate venv
- - Linux: ```source venv/scripts/activate```
- - Windows: ```venv/Scripts/activate```
- Install dependencies: 
- - ```pip install python-decouple psycopg2 sqlalchemy scrapy pytest``` (avoid using requirements.txt)
- Configure settings
- - Files: ```src/dbm/settings.py```
- Run tests 
- - ```python scripts/testing/run_tests.py```

TODO:
- Logger package
- deploy.sh ()