# main.py
# import nltk
from flask import request
from flask import jsonify
from flask import Flask, render_template
import json
import subprocess
import sentencepiece as spm
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# app = Flask(__name__)
#modifying the backend


import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "7"
import logging
# import sacrebleu
import pandas as pd
from simpletransformers.t5 import T5Model, T5Args


logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)


model_args = T5Args()
model_args.max_length = 256
model_args.n_gpu = 4
model_args.length_penalty = 1
model_args.num_beams = 10
model_args.use_cuda = False
model_args.use_multiprocessed_decoding = False
# model_output_dir = "/home/mohammed_yahia3/checkpoint-49960-epoch-8"
model_output_dir="/home/CE/musaeed/checkpoint-124900-epoch-8"
model_output_dir = "/home/CE/musaeed/checkpoint-140600-epoch-3"
model_output_dir = "/home/CE/musaeed/checkpoint-185000-epoch-9"
# model = T5Model("t5", model_output_dir, args=model_args, use_cuda=True)
model = T5Model("t5", model_output_dir, args=model_args, use_cuda=False)


 

# sentence = ["translate english to pcm: how to have sex with girl until she cries",
#             "translate pcm to english: ‘ Make una be people wey like peace . ’ — MARK 9 : 50 .?"]

# pcm_preds = model.predict(sentence)
# print(f"the prediction is {pcm_preds}")


pcm_en_calling = "/home/CE/musaeed/translation_app/mt_interface/test.sh"
en_pcm_calling= "/home/CE/musaeed/translation_app/mt_interface/test_en_pcm.sh"
@app.route('/')
def my_form():
    return render_template('index.html')
file = "models.txt"






@app.route('/pcm_en', methods=['POST'])
def my_form_post():
    requestBody = request.get_json()
    text = requestBody['details']
    # print(f"the type of detail is {text}")
    # subprocess.call(save_line)
    # machine_translated = pcm2en.translate(text)
    text_array = text.split(".")
    text_array = list(filter(lambda x: x.strip(), text_array))
    # sentence = ["translate pcm to english: " + str(text)]
    sentence = ["translate pcm to english: " + r for r in text_array]
    text_ = model.predict(sentence)
    translation = ". ".join(text_) + "."
    machine_translated=translation
    print(f"the translated text is {machine_translated}")
    # write_file(text)
    # call_pcm_en()
    # machine_translated = pcm_en_mt_out_processing()
    # # machine_translated = text
    # encode_en = en_model.encode(machine_translated)
    # machine_translated = en_model.decode(encode_en)
    return({"translatedDetails": machine_translated})


@app.route('/enpcm', methods=['POST'])
def my_form_post_en_pcm():
    requestBody = request.get_json()
    print("here")
    text = requestBody['details']
    print(f"the type of detail is {text}")
    # subprocess.call(save_line)
    text_array = text.split(".")
    text_array = list(filter(lambda x: x.strip(), text_array))
    # sentence = ["translate pcm to english: " + str(text)]
    sentence = ["translate english to pcm: " + r for r  in text_array]
    # sentence = ["translate english to pcm: " + str(text)]
    print(sentence)
    text_ = model.predict(sentence)
    print(text_)
    translation = ". ".join(text_)+"."
    # machine_translated = en2pcm.translate(text)
    # machine_translated = text_[0]
    machine_translated= translation

    # write_file_en(text)
    print("reached here")
    print(f"the translated text is {machine_translated}")
    # call_en_pcm()
    # machine_translated = en_pcm_mt_out_processing()
    # # machine_translated = text
    # encode_pcm = pcm_model.encode(machine_translated)
    # machine_translated = pcm_model.decode(encode_pcm)

    return({"translatedDetails": machine_translated})
if __name__ == "__main__":
    app.run(port=8000, threaded=True, debug=True)
