from src.__init__ import *
from settings import DATABASE, USER
app = create_app(database = DATABASE, user = USER)
app.run(debug = True)

