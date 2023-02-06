

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
model_output_dir="/home/CE/musaeed/checkpoint-185000-epoch-9"
model = T5Model("t5", model_output_dir, args=model_args, use_cuda=True)

pcmTEXT = "The girl I love doesnot allow me to say I love you. However I love her"

text_array = pcmTEXT.split(".")
sentences = [ "translate english to pcm: " +r for r in text_array]
print(sentences)
text_ = model.predict(sentences)
# machine_translated = en2pcm.translate(text)
machine_translated = text_
translated = [r +"." for r in machine_translated]
# machine_translated.append(machine_translated)
print(f"machine translated {text_}")
# text_.extend(text_)

print("\n. ".join(text_) +"." )