from flask import Flask, Response, request , jsonify 
import sys
project_name = "./Real_Time_Voice_Cloning"
sys.path.append(project_name)

import Real_Time_Voice_Cloning.model as model
import base64
import json
from connect import db,Tales
import logging

import gzip
# configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://lumineuxp:hgnuPHIJS9O7@ep-raspy-hall-234246.ap-southeast-1.aws.neon.tech/syn_voice_app"
db.init_app(app)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/api-embed', methods=['POST'])
def get_embed():
    wav_file64= request.json['wav']
    embed64 = model.get_embed(wav_file64) #base64
    ex_syn = model.get_ex_syn(embed64)
    embed64_tostr = embed64.decode('utf8').replace("'", '"')
    syn_tostr = ex_syn.decode('utf8').replace("'", '"')
    
    jsonstr = {
        'embed': embed64_tostr,
        'ex_synthesize_voice' : syn_tostr
        
    } 
    
    # json_data = json.dumps(jsonstr)   ,ex_synthesize_voice=syn_tostr
    compressed_data = gzip.compress(jsonify(jsonstr).data)
    
    #  jsonify(embed=embed64_tostr,ex_synthesize_voice=syn_tostr)
    return Response(compressed_data, mimetype='application/json', headers={'Content-Encoding': 'gzip'})
    # return jsonify(embed=embed64_tostr,ex_synthesize_voice=syn_tostr)
    
@app.route('/api-synthesize-tale', methods=['POST'])
def get_synthesize_tale():
    tale_id = request.json['tale_id'] #connect database
    embed64 = bytes(request.json['embed'], 'utf-8')
    
    tales = Tales.query.filter_by(id=tale_id).first()
    story = tales.story
    
    texts = story.split('/')
    
    syn_texts = []
    for text in texts: 
        syn = model.get_syn_voice(embed64,text) #base64
        # print(type(text))
        syn_tostr = syn.decode('utf8').replace("'", '"')
        jsonobj = {
            'text':text,
            'syn_voice': syn_tostr
        } 
        syn_texts.append(jsonobj)
        
    jsonstr = {
            'tale_id': tale_id,
            'syn_voice': syn_texts
        }  
    json_data = json.dumps(jsonstr)
    return json_data

@app.route('/get_tales')
def get_tales():
    tales_db = db.session.execute(db.select(Tales).order_by(Tales.id)).all()
    
    tales = []
    for tale in tales_db :
        
        jsonstr = {
            'tald_id': tale[0].id,
            'cover' : tale[0].cover_img,
            'title' : tale[0].title,
            'story' : tale[0].story
        } 
        tales.append(jsonstr)
     
    json_data = json.dumps(tales)
    return json_data


if __name__ == "__main__":

    app.run(debug = True)

