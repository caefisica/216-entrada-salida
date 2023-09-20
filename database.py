import os
import pandas as pandas
from main import *

name = os.getenv('name')
last_name = os.getenv('last_name')

user = str(name) + str(last_name)