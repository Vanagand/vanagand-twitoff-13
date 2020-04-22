# vanagand-twitoff-13

## Installation

TODO: [summary]

## Setup

TODO: [summary]

Migrate the database:

'''sh
# Windows users can omit the "FLASK_APP=web_app" part...
FLASK_APP=web_app flask db init #> generates app/migrations dir
FLASK_APP=web_app flask db migrate #> creates the db
FLASK_APP=web_app flask db upgrade #> creates the specified tables
'''

## Use

"""[summary]
"""