#!/bin/sh

input_file="/home/CE/musaeed/translation_app/mt_interface/english_to_pcm_true/data_folders/mt_output.txt"
# path="/home/CE/musaeed/ironside/back_translation_joint_vocab_checkpoint/Jones_BT_config_validation_joint_data_bpe_en_pcm_6_l_4_h_256_embedd_64_b_1024_ffnn_checkpoints/checkpoint_last.pt"
path="/home/CE/musaeed/shallow_model_en_pcm/real_data_en_pcm_1_layer_2_heads_512_embedddings_512_ffnn/checkpoint_last.pt"
# CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=1,2,3,4,5,6
fairseq-interactive \
"/home/CE/musaeed/ironside/Machine_Translation/back_translation/JW300_with_bible_joined_embeddings/BT_en_pcm.tokenized.en-pcm" \
--input $input_file \
--cpu \
--path $path \
--buffer-size 2048 --beam 5 --batch-size 2048 \
--skip-invalid-size-inputs-valid-test >/home/CE/musaeed/translation_app/mt_interface/english_to_pcm_true/pcm_en_mt_output.txt