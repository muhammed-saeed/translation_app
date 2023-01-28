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

pcm_model_spm = "/home/CE/musaeed/ironside/bpe_dict_path/pcm__vocab_4000.model"
en_model_spm = "/home/CE/musaeed/ironside/JW300_with_bible_joined_embeddings/bpe_dict_path/en__vocab_4000.model"

pcm_model = spm.SentencePieceProcessor(pcm_model_spm)
en_model = spm.SentencePieceProcessor(en_model_spm)
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
model_args.use_multiprocessed_decoding = False
# model_output_dir = "/home/mohammed_yahia3/checkpoint-49960-epoch-8"
model_output_dir="/home/CE/musaeed/checkpoint-124900-epoch-8"
model_output_dir = "/home/CE/musaeed/checkpoint-140600-epoch-3"
model_output_dir = "/home/CE/musaeed/checkpoint-185000-epoch-9"
model = T5Model("t5", model_output_dir, args=model_args, use_cuda=True)

 

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

from fairseq.models.transformer import TransformerModel
en2pcm_large_model_path="/home/CE/musaeed/ironside/back_translation_joint_vocab_checkpoint/Jones_BT_config_validation_joint_data_bpe_en_pcm_6_l_4_h_256_embedd_64_b_1024_ffnn_checkpoints/"
en2pcm_small_model_path='/home/CE/musaeed/shallow_model_en_pcm/real_data_en_pcm_1_layer_2_heads_512_embedddings_512_ffnn/'
en2pcm_preprocess_large="/home/CE/musaeed/ironside/Machine_Translation/back_translation/JW300_with_bible_joined_embeddings/BT_en_pcm.tokenized.en-pcm"
en2pcm_preprocess_small='/home/CE/musaeed/auto-annotator/kd-distiller/JW300_with_bible_joined_embeddings/FAKE_en_pcm.tokenized.en-pcm'
en2pcm = TransformerModel.from_pretrained(
  en2pcm_large_model_path,
  checkpoint_file='checkpoint_last.pt',
  data_name_or_path=en2pcm_preprocess_large,
  bpe='sentencepiece',
  sentencepiece_model='/home/CE/musaeed/auto-annotator/kd-distiller/JW300_with_bible_joined_embeddings/bpe_dict_path/en__vocab_4000.model'
)
pcm2en_large_model_path="/home/CE/musaeed/pcm_en/"
pcm2en_small_model_path='/home/CE/musaeed/kd-distiller/checkpoints/pcm_en_1_layer_512_embedddings_512_ffnn/'
pcm2en_small_model_preprocess='/home/CE/musaeed/auto-annotator/kd-distiller/JW300_with_bible_joined_embeddings/FAKE_pcm_en.tokenized.pcm-en'
pcm2en_large_model_preprocess="/home/CE/musaeed/pcm_en/BT_pcm_en.tokenized.pcm-en"
pcm2en =  TransformerModel.from_pretrained(pcm2en_large_model_path
  ,
  checkpoint_file='checkpoint_last.pt',
  data_name_or_path=pcm2en_large_model_preprocess,
  bpe='sentencepiece',
  sentencepiece_model='/home/CE/musaeed/auto-annotator/kd-distiller/JW300_with_bible_joined_embeddings/bpe_dict_path/pcm__vocab_4000.model'
)

# a = en2pcm.translate("there was god at the beginning")




def save_line(details):
    with open(file, 'w') as fb:
        json.dump(details, fb)


def write_file(text):
    # with open("/home/CE/musaeed/mt_interface/english_to_pcm/data_folders/mt_source_input.txt","w") as fb:
    with open("/home/CE/musaeed/translation_app/mt_interface/english_to_pcm/data_folders/mt_source_input.txt","w") as fb:
 
        fb.write(text)


def write_file_en(text):
    with open("/home/CE/musaeed/translation_app/mt_interface/english_to_pcm_true/data_folders/mt_source_input.txt","w") as fb:
        fb.write(text)

def call_pcm_en():
    subprocess.call(pcm_en_calling)

def call_en_pcm():
    subprocess.call(en_pcm_calling)

def pcm_en_mt_out_processing():
    pcm_en_output = []
    pcm_en_output_response=""
    with open("/home/CE/musaeed/translation_app/mt_interface/english_to_pcm/pcm_en_mt_output.txt", "r") as fb:
        pcm_en_output = fb.readlines()
    for line in pcm_en_output:
        if "H-0	" in line:
            pcm_en_output_response = ''.join(line.split()[2:])
            # print(line.split()[2:])

    return pcm_en_output_response




def en_pcm_mt_out_processing():
    pcm_en_output = []
    pcm_en_output_response=""
    with open("/home/CE/musaeed/translation_app/mt_interface/english_to_pcm_true/pcm_en_mt_output.txt", "r") as fb:
        pcm_en_output = fb.readlines()

    for line in pcm_en_output:
        if "H-0	" in line:
            pcm_en_output_response = ''.join(line.split()[2:])
            # print(line.split()[2:])

    return pcm_en_output_response





@app.route('/pcm_en', methods=['POST'])
def my_form_post():
    requestBody = request.get_json()
    text = requestBody['details']
    # print(f"the type of detail is {text}")
    # subprocess.call(save_line)
    # machine_translated = pcm2en.translate(text)
    sentence = ["translate pcm to english: " + str(text)]
    text_ = model.predict(sentence)
    machine_translated=text_[0]
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
    sentence = ["translate english to pcm: " + str(text)]
    text_ = model.predict(sentence)
    # machine_translated = en2pcm.translate(text)
    machine_translated = text_[0]

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
