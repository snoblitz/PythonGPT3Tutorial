# This code uses the OpenAI GPT-3 API to generate a conversation between a user and a fictional character from the Destiny 2 universe, Rasputin
import openai
import pandas as pd


# Function to read a file containing the user's OpenAI API key
def open_file(filepath):
	with open(filepath, 'r', encoding='utf-8') as infile:
		return infile.read()


# Set the API key
openai.api_key = open_file('openaiapikey.txt')


# Function to generate a response to the user's input based on the OpenAI GPT-3 model
def gpt3_completion(prompt, engine='text-davinci-003', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['RASPUTIN:', 'GUARDIAN:']):
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


# Initiate a conversation with Rasputin, in which the user's input is read and then passed to the gpt3_completion() function, which generates a response from Rasputin. The conversation is then printed to the console.
if __name__ == '__main__':
    conversation = list()
    while True:
        user_input = input('GUARDIAN: ')
        conversation.append('GUARDIAN: %s' % user_input)
        text_block = '/n'.join(conversation)
        prompt = open_file('prompt_chat_rasputin.txt').replace('<<BLOCK>>', text_block)
        prompt = prompt + '/nRASPUTIN: '
        response = gpt3_completion(prompt)
        print('RASPUTIN:', response)
        conversation.append('RASPUTIN: %s' % response)