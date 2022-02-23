import pip

pip.main(['install','-q', '-r', 'requirements.txt'])

import os
import scrapy
import json
import re
from dotenv import load_dotenv, dotenv_values
load_dotenv()
config = dotenv_values('.env')
print(config)