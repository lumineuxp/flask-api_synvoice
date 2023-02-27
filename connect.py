# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import psycopg2
# from IPython.display import display, HTML # used to print out pretty pandas dataframes
# import matplotlib.dates as dates
# import matplotlib.lines as mlines

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()

class Tales(db.Model):
    __tablename__ = "tales"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    story = db.Column(db.String, nullable=False) 
    cover_img = db.Column(db.String, nullable=False)