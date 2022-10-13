
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

article_hi = "संयुक्त राष्ट्र के प्रमुख का कहना है कि सीरिया में कोई सैन्य समाधान नहीं है"
article_ar = "الأمين العام للأمم المتحدة يقول إنه لا يوجد حل عسكري في سوريا."

model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

# translate Hindi to French
tokenizer.src_lang = "hi_IN"
encoded_hi = tokenizer(article_hi, return_tensors="pt")
generated_tokens = model.generate(**encoded_hi, forced_bos_token_id=tokenizer.lang_code_to_id["fr_XX"])
decoded= tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
print(f"the translated is {decoded}")
# => "Le chef de l 'ONU affirme qu 'il n 'y a pas de solution militaire en Syria."

# translate Arabic to English
tokenizer.src_lang = "ar_AR"
encoded_ar = tokenizer(article_ar, return_tensors="pt")
generated_tokens = model.generate(**encoded_ar, forced_bos_token_id=tokenizer.lang_code_to_id["en_XX"])
decoded = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
print(decoded)
# translate English to Arabic

tokenizer.src_lang = "en_EN"
article_en = "Why you don't have hair?"
encoded_ar = tokenizer(article_en, return_tensors="pt")
generated_tokens = model.generate(**encoded_ar, forced_bos_token_id=tokenizer.lang_code_to_id["ar_AR"])
decoded = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
print(decoded[0])
print(type(decoded))
with open("/home/CE/musaeed/translation_app/mbart/decoded.txt", "w") as fb:
    fb.write(str(decoded))

#######################################
from transformers import MBartTokenizerFast

tokenizer = MBartTokenizerFast.from_pretrained(
    "facebook/mbart-large-en-ro", src_lang="en_XX", tgt_lang="ar_AR"
)
example_english_phrase = " UN Chief Says There Is No Military Solution in Syria"
expected_translation_romanian = "Şeful ONU declară că nu există o soluţie militară în Siria"
inputs = tokenizer(example_english_phrase, text_target=expected_translation_romanian, return_tensors="pt")
