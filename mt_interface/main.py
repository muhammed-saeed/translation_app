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


pcm_model_spm = "/home/mohammed_yahia3/bpe_dict_path/pcm__vocab_4000.model"
en_model_spm = "/home/mohammed_yahia3/bpe_dict_path/en__vocab_4000.model"

pcm_model = spm.SentencePieceProcessor(pcm_model_spm)
en_model = spm.SentencePieceProcessor(en_model_spm)



pcm_en_calling = "/home/CE/musaeed/translation_app/mt_interface/test.sh"
en_pcm_calling= "/home/CE/musaeed/translation_app/mt_interface/test_en_pcm.sh"

def my_form():
    return render_template('index.html')



from fairseq.models.transformer import TransformerModel
en2pcm_large_model_path="/home/CE/musaeed/ironside/back_translation_joint_vocab_checkpoint/Jones_BT_config_validation_joint_data_bpe_en_pcm_6_l_4_h_256_embedd_64_b_1024_ffnn_checkpoints/"


# +
from fairseq.models.transformer import TransformerModel
en2pcm_large_model_path="/home/mohammed_yahia3/Jones_BT_config_validation_joint_data_bpe_en_pcm_6_l_4_h_256_embedd_64_b_1024_ffnn_checkpoints/"
en2pcm_small_model_path='/home/CE/musaeed/shallow_model_en_pcm/real_data_en_pcm_1_layer_2_heads_512_embedddings_512_ffnn/'
en2pcm_preprocess_large="/home/mohammed_yahia3/Jones_BT_config_validation_joint_data_bpe_en_pcm_6_l_4_h_256_embedd_64_b_1024_ffnn_checkpoints/BT_en_pcm.tokenized.en-pcm"
en2pcm_preprocess_small='/home/CE/musaeed/auto-annotator/kd-distiller/JW300_with_bible_joined_embeddings/FAKE_en_pcm.tokenized.en-pcm'

'''
en2pcm = TransformerModel.from_pretrained(
  en2pcm_large_model_path,
  checkpoint_file='checkpoint_last.pt',
  data_name_or_path=en2pcm_preprocess_large,
  bpe='sentencepiece',
  sentencepiece_model=en_model_spm
)
'''

pcm2en_large_model_path="/home/mohammed_yahia3/JW300_with_bible_joined_embeddings_back_translation_pcm_to_real_english/pcm_en_sh_decoder_1L_2h_512_550_epochs/"
pcm2en_small_model_path="/home/mohammed_yahia3/JW300_with_bible_joined_embeddings_back_translation_pcm_to_real_english/pcm_en_sh_decoder_1L_2h_512_550_epochs/"
pcm2en_small_model_preprocess="/home/mohammed_yahia3/JW300_with_bible_joined_embeddings_back_translation_pcm_to_real_english/shallow_pcm_en.tokenized.pcm-en" 
pcm2en_large_model_preprocess="/home/mohammed_yahia3/pcm_en/BT_pcm_en.tokenized.pcm-en"
pcm2en =  TransformerModel.from_pretrained(pcm2en_small_model_path
  ,
  checkpoint_file='checkpoint_last.pt',
  data_name_or_path=pcm2en_small_model_preprocess,
  bpe='sentencepiece',
  sentencepiece_model=pcm_model_spm
)





from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")



# # translate Arabic to English
# tokenizer.src_lang = "ar_AR"
# article_ar = "السلام عليكم كيف حالك  "
# encoded_ar = tokenizer(article_ar, return_tensors="pt")
# generated_tokens = model.generate(**encoded_ar, forced_bos_token_id=tokenizer.lang_code_to_id["en_XX"])
# decoded = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
# print(decoded[0])

# translate English to Arabic
# tokenizer.src_lang = "en_EN"
# article_en = "Why you don't have hair?"
# encoded_ar = tokenizer(article_en, return_tensors="pt")
# generated_tokens = model.generate(**encoded_ar, forced_bos_token_id=tokenizer.lang_code_to_id["ar_AR"])
# decoded = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
# print(decoded[0])




@app.route('/pcm_en', methods=['POST'])
def my_form_post():
    requestBody = request.get_json()
    text = requestBody['details']
    
   
    machine_translated = pcm2en.translate(text)

    print(f"the translated text is {machine_translated}")



    return({"translatedDetails": machine_translated})


@app.route('/enpcm', methods=['POST'])
def my_form_post_en_pcm():
    requestBody = request.get_json()
    print("here")
    text = requestBody['details']
    print(f"the type of detail is {text}")
    machine_translated = text

 
    return({"translatedDetails": machine_translated})


@app.route('/en2ar', methods=['POST'])
def my_form_post_en_ar():
    requestBody = request.get_json()
    print("here")
    text = requestBody['details']
    print("#######EN2AR########")    
    machine_translated = text
    print(f"the text to be translated is {text}")
    tokenizer.src_lang = "en"
    english_text = str(text)
    encoded_zh = tokenizer(english_text, return_tensors="pt")
    generated_tokens = model.generate(**encoded_zh, forced_bos_token_id=tokenizer.get_lang_id("ar"))
    arabic_output = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    print(f"the arabic output is {arabic_output}")
    print("##################")
    # print(machine_translated)
    machine_translated  = arabic_output[0]
 
    return({"translatedDetails": machine_translated})

if __name__ == "__main__":
    app.run(port=8000, threaded=False, debug=True)
