pcm_english_model = "/home/CE/musaeed/ironside_2/ironside/Machine_Translation/back_translation_checkpoints/BT_config_validation_joint_data_bpe_pcm_en_6_l_4_h_256_embedd_64_b_1024_ffnn_checkpoints/checkpoint_best.pt"


import os

import subprocess
# bpe="/home/CE/musaeed/mt_interface/bpe_english_.py"
# bpe_sh="/home/CE/musaeed/mt_interface/english_to_pcm/bpe_shell.sh"
bpe_sh="/home/CE/musaeed/mt_interface/english_to_pcm/pcm_bpe_shell.sh"
fairseq_interactive = "/home/CE/musaeed/mt_interface/english_to_pcm/fairseq_interactive_bpe_non_interactive.sh"
# with open(cmd,'w') as f: f.write('#!/bin/sh\nexit 0')

# os.execl('/home/CE/musaeed/mt_interface/fairseq_interactive_bpe_non_interactive.sh', '/home/CE/musaeed/mt_interface/fairseq_interactive_bpe_non_interactive.sh')
rc=subprocess.call(bpe_sh)
rc = subprocess.call(fairseq_interactive)
print(rc)













# fairseq-interactive --input="google is awesome" [all-your-fairseq-parameters] > target.txt
# from fairseq.models.transformer import TransformerModel
# trans = TransformerModel.from_pretrained(
#   '/model',
#   checkpoint_file='checkpoint_best.pt',
#   data_name_or_path='bin/',
#   is_gpu=True
# ).cuda()
# inputs = "Di-mairt Clodh-bhualadh a cheud leabhair,"
# print(trans.translate(inputs))

# from transformers import FSMTForConditionalGeneration, FSMTTokenizer
# mname = "facebook/wmt19-en-de"
# tokenizer = FSMTTokenizer.from_pretrained(mname)
# model = FSMTForConditionalGeneration.from_pretrained(pcm_english_model)

# input = "Machine learning is great, isn't it?"
# input_ids = tokenizer.encode(input, return_tensors="pt")
# outputs = model.generate(input_ids)
# decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
# print(decoded) # Maschinelles Lernen ist großartig, oder?