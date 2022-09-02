# /home/CE/musaeed/ironside_3/ironside/bpe_dict_path/pcm__vocab_4000.vocab

import sentencepiece as spm

en_tokenizer = spm.SentencePieceProcessor(model_file="/home/CE/musaeed/ironside_2/ironside/bpe_dict_path/pcm__vocab_4000.model")
# pcm_tokenizer = spm.SentencePieceProcessor(model_file="/home/CE/musaeed/ironside/bpe_dict_path/pcm__vocab_4000.model")

mt_interface_input="/home/CE/musaeed/mt_interface/english_to_pcm/data_folders/mt_source_input.txt"
# pcm_mono_bpe_token="/home/CE/musaeed/ironside_2/ironside/Machine_Translation/back_translation/en_back_tranlsation_data_bpe.txt"
mt_interface_output="/home/CE/musaeed/mt_interface/english_to_pcm/data_folders/mt_output.txt"
with open(mt_interface_input, "r", encoding="utf-8") as rf, open(mt_interface_output, "w", encoding="utf-8") as wf:
    output_lines = []
    for line in rf.readlines():
        wf.write(' '.join(en_tokenizer.encode(line, out_type=str)))
        # output_lines.append(tokenizer.encode(input = line, out_type = str))
        wf.write("\n")

    # wf.writelines(str(output_lines))