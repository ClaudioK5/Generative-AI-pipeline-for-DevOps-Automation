import openai

openai.api_key = "insert here your openai api key"


def generate(log_content_before, log_content_after, Python_Script_description):
    part0 = '''\n Hello ChatGPT, listen you have a task: the user will operate on the folder path a python script. You will be provided with the descriptio of how the Python script works. Then you will be given an overview of the internal structure of the folder path BEFORE the script was run and AFTER it was run and you should see whether it has worked or not. \n'''
    part1 = '''\n The following Python script is designed to perform the task described below:\n\n'''
    part2 = '''\n The folder structure shown below is the directory BEFORE the script operated on. It is provided to give you context - it is **not** the output of the script. \n'''
    part3 = '''\n Folder structure scanned:\n'''
    part4 = '''\n The folder structure shown below is the directory AFTER the script operated on. It is provided to give you context - it is **not** the output of the script. \n'''

    new_prompt = part0 + part1 + Python_Script_description + part2 + part3 + log_content_before + part4 + part3 + log_content_after + '''Please let me know: Based upon the main objective of the script, does it appear to be working correctly? (be ware, after each point · it is indicated the name of a unique file.)'''

    print(new_prompt)

    response = openai.chat.completions.create(model="gpt-3.5-turbo",
                                              messages=[{'role': 'user', 'content': new_prompt}],
                                              max_tokens=150)

    ai_output = response.choices[0].message.content.strip()

    return ai_output
