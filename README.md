# web_app01


# Installation

 '''sh
 git clone git@github.com/techthumb1/web_app01.git
 cd web_app01
 '''

 # Setup

 '''sh
 pipenv install
 '''

 Migrate the database:

 '''sh
 FLASK_APP=web_app01 flask db init
 FLASK_APP=web_app01 flask db migrate
 FLASK_APP=web_app01 flask db upgrade
 '''

 # Usage

'''sh
FLASK_APP=web_app01 flask run
'''
