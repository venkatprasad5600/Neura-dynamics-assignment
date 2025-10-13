from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration

# Load pretrained RAG model
tokenizer = RagTokenizer.from_pretrained("facebook/rag-sequence-base")
retriever = RagRetriever.from_pretrained("facebook/rag-sequence-base", index_name="custom", passages_path=None)
model = RagSequenceForGeneration.from_pretrained("facebook/rag-sequence-base", retriever=retriever)

def answer_question(question):
    inputs = tokenizer([question], return_tensors="pt")
    generated = model.generate(input_ids=inputs['input_ids'])
    answer = tokenizer.batch_decode(generated, skip_special_tokens=True)[0]
    return answer

if __name__ == "__main__":
    question = "What is the revenue of Company X in Q2 2023?"
    print("Answer:", answer_question(question))
