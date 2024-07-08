from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = 'gpt2'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)


def generate_article(sentences):
    prompt = "\n".join(sentences)[:1024]

    
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    
    outputs = model.generate(inputs, max_length=1024, num_return_sequences=1, no_repeat_ngram_size=2, early_stopping=True)
    
    article = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return article
