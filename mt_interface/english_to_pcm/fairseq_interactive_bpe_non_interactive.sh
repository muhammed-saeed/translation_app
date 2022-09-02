#!/bin/sh

input_file="/home/CE/musaeed/mt_interface/english_to_pcm/data_folders/mt_output.txt"
path="/home/CE/musaeed/ironside_2/ironside/Machine_Translation/back_translation_checkpoints/BT_config_validation_joint_data_bpe_pcm_en_6_l_4_h_256_embedd_64_b_1024_ffnn_checkpoints/checkpoint_last.pt"

CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=1,2,3,4,5,6 fairseq-interactive \
"/home/CE/musaeed/ironside_2/ironside/JW300_with_bible_joined_embeddings/bpe_vocab_bpe_en_pcm.tokenized.en-pcm" \
--input $input_file \
--path $path \
--buffer-size 512 --beam 5 --batch-size 256 \
--skip-invalid-size-inputs-valid-test >/home/CE/musaeed/mt_interface/english_to_pcm/pcm_en_mt_output.txt