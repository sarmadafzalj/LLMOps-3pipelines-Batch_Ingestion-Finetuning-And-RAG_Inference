from datasets import load_dataset, DatasetDict

dataset = load_dataset("vicgalle/alpaca-gpt4")
print(dataset)

top_10_rows = dataset['train']
print(top_10_rows)

print(top_10_rows[0])