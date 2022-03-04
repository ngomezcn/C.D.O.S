Create venv python -m venv venv 
Linux 
source venv/scripts/activate
Windows 
venv/Scripts/activate

Setup:
pip install --upgrade pip

Install dependencies:
pip install python-decouple psycopg2 sqlalchemy scrapy pytest (Recommended)
or 
pip install -r requeriments.txt

Run tests:
python scripts/testing/run_tests.py