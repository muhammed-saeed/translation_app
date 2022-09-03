# main.py
# import nltk
from flask import request
from flask import jsonify
from flask import Flask, render_template
import json
import subprocess
app = Flask(__name__)
pcm_en_calling = "/home/CE/musaeed/mt_interface/test.sh"

@app.route('/')
def my_form():
    return render_template('index.html')
file = r"C:\Users\lst\Documents\translation_app\mt_interface\models.txt"
def save_line(details):
    with open(file, 'w') as fb:
        json.dump(details, fb)


def write_file(text):
    with open("/home/CE/musaeed/mt_interface/english_to_pcm/data_folders/mt_source_input.txt","w") as fb:
        fb.write(text)

def call_pcm_en():
    subprocess.call(pcm_en_calling)

def pcm_en_mt_out_processing():
    pcm_en_output = []
    pcm_en_output_response=""
    with open("/home/CE/musaeed/mt_interface/english_to_pcm/pcm_en_mt_output.txt", "r") as fb:
        pcm_en_output = fb.readlines()
    for line in pcm_en_output:
        if "H-0	" in line:
            pcm_en_output_response = ''.join(line.split()[2:])
            # print(line.split()[2:])

    return pcm_en_output_response



@app.route('/', methods=['POST'])
def my_form_post():
    requestBody = request.get_json()
    text = requestBody['details']
    print(f"the type of detail is {text}")
    subprocess.call(save_line)
    write_file(text)
    call_pcm_en()
    machine_translated = pcm_en_mt_out_processing()

    return({"translatedDetails": machine_translated})

if __name__ == "__main__":
    app.run(port='8000', threaded=False, debug=True)