# import sys
# project_name = "./Real_Time_Voice_Cloning"
# sys.path.append(project_name)

import numpy as np
from datetime import datetime
import os

from synthesizer.inference import Synthesizer
from encoder import inference as encoder
from vocoder import inference as vocoder

import base64
import soundfile as sf

import asyncio

encoder.load_model("./Real_Time_Voice_Cloning/saved_models/default/encoder.pt")
synthesizer = Synthesizer("./Real_Time_Voice_Cloning/saved_models/default/synthesizer.pt")
vocoder.load_model("./Real_Time_Voice_Cloning/saved_models/default/vocoder.pt")

SAMPLE_RATE = 22050
audio = "Record" 

def _compute_embedding(audio):
    embedding = encoder.embed_utterance(encoder.preprocess_wav(audio, SAMPLE_RATE))
    return embedding

def synthesize(embed, text ):
    print("Synthesizing new audio...")
    
    specs = synthesizer.synthesize_spectrograms([text], [embed])
    generated_wav = vocoder.infer_waveform(specs[0])
    generated_wav = np.pad(generated_wav, (0, synthesizer.sample_rate), mode="constant")
    return generated_wav

def get_embed(voice_encode64):
    gen_file_name = generate_file_name_from_time()
    file_name = "{}.wav".format(gen_file_name)
    
    #convert voice encode to voice file 
    voice = base64.b64decode(voice_encode64)
    with open(file_name, "wb") as wav_file:
        wav_file.write(voice)   
    
    embed = _compute_embedding(file_name)
      
    #convert embed to base64
    embed64 = base64.b64encode(embed)
    
    os.remove(file_name)
    # embed64_tostr = embed64.decode('utf8').replace("'", '"')
    return embed64

def get_syn_voice(embed64,text): 
    gen_file_name = generate_file_name_from_time()
    file_name = "syn{}.mp3".format(gen_file_name)
    
    embed_decode = base64.b64decode(embed64) #decode embed64 
    embed = np.frombuffer(embed_decode, dtype=np.float32) #convert embbed_decode to numpy form.
    
    synthesized_voice = synthesize(embed, text)
    #save audio
    sf.write(file_name, synthesized_voice, synthesizer.sample_rate,format='MP3')  
    #convert synthesized voice to base64
    with open(file_name, "rb") as file: 
        encode_string = base64.b64encode(file.read())
    
    os.remove(file_name)
    return encode_string

def get_ex_syn(embed64):
    text = "A MONKEY perched upon a lofty tree saw some Fishermen casting their nets into a river, and narrowly watched their proceedings."
    
    encode_syn_voice = get_syn_voice(embed64, text)
    

    return encode_syn_voice

def generate_file_name_from_time():
    dt = datetime.utcnow().strftime('%Y%m%d-%H%M%S%f')
    return dt