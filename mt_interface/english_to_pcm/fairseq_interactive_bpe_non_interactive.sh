#!/bin/sh

input_file="/home/CE/musaeed/translation_app/mt_interface/english_to_pcm/data_folders/mt_output.txt"
# path="/home/CE/musaeed/pcm_en/checkpoint_last.pt"
path="/home/CE/musaeed/kd-distiller/checkpoints/pcm_en_1_layer_512_embedddings_512_ffnn/checkpoint_last.pt"
# CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=1,2,3,4,5,6 
fairseq-interactive \
"/home/CE/musaeed/pcm_en/BT_pcm_en.tokenized.pcm-en" \
--input $input_file \
--cpu \
--path $path \
--buffer-size 4096 --beam 5 --batch-size 4096 \
--skip-invalid-size-inputs-valid-test >/home/CE/musaeed/translation_app/mt_interface/english_to_pcm/pcm_en_mt_output.txt