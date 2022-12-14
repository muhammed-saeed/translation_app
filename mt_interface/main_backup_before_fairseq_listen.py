# main.py
# import nltk
from flask import request
from flask import jsonify
from flask import Flask, render_template
import json
import subprocess
import sentencepiece as spm
app = Flask(__name__)

pcm_model_spm = "/home/CE/musaeed/ironside/bpe_dict_path/pcm__vocab_4000.model"
en_model_spm = "/home/CE/musaeed/ironside/JW300_with_bible_joined_embeddings/bpe_dict_path/en__vocab_4000.model"

pcm_model = spm.SentencePieceProcessor(pcm_model_spm)
en_model = spm.SentencePieceProcessor(en_model_spm)



pcm_en_calling = "/home/CE/musaeed/translation_app/mt_interface/test.sh"
en_pcm_calling= "/home/CE/musaeed/translation_app/mt_interface/test_en_pcm.sh"
@app.route('/')
def my_form():
    return render_template('index.html')
file = "models.txt"
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
    write_file(text)
    call_pcm_en()
    machine_translated = pcm_en_mt_out_processing()
    # machine_translated = text
    encode_en = en_model.encode(machine_translated)
    machine_translated = en_model.decode(encode_en)
    return({"translatedDetails": machine_translated})


@app.route('/enpcm', methods=['POST'])
def my_form_post_en_pcm():
    requestBody = request.get_json()
    print("here")
    text = requestBody['details']
    print(f"the type of detail is {text}")
    # subprocess.call(save_line)
    write_file_en(text)
    print("reached here")
    call_en_pcm()
    machine_translated = en_pcm_mt_out_processing()
    # machine_translated = text
    encode_pcm = pcm_model.encode(machine_translated)
    machine_translated = pcm_model.decode(encode_pcm)
    return({"translatedDetails": machine_translated})
if __name__ == "__main__":
    app.run(port=8000, threaded=False, debug=True)
