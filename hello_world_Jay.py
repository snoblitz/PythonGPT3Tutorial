import openai
import pandas as pd


def open_file(filepath):
	with open(filepath, 'r', encoding='utf-8') as infile:
		return infile.read()


openai.api_key = open_file('PythonGPT3Tutorial\openaiapikey.txt')


def gpt3_completion(prompt, engine='text-davinci-003', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['JAX:', 'USER:']):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
    text = response['choices'][0]['text'].strip()
    return text


if __name__ == '__main__':
	prompt = 'Write a list of five famous non-American actors:'
	response = gpt3_completion(prompt)
	print(response)