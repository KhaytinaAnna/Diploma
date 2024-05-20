import openai
import json
import os
import dotenv

import subprocess


dotenv.load_dotenv()
openai.api_key = os.getenv("CHATGPT_AUTH")

'''
In the system:
export START_TEST=0
export END_TEST=163
'''

start_test = int(os.environ.get("START_TEST"))
end_test = int(os.environ.get("END_TEST"))



def f(method, coverage_sequence):
    response = openai.ChatCompletion.create(
        #   model="gpt-3.5-turbo",
        model="gpt-4-turbo",
        messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Внимание: не пиши ничего лишнего в ответе, только данные, которые подаются на вход, без дополнительных пояснений и комментариев. \n\n Предварительная информация: символ > означает, что строка кода исполняется, символ ! означает, что строка кода не исполняется. \n\n Напиши такие входные данные для функции, описанной в method: \n\n {method} \n\n на которых будут исполнены строчки, которые помечены > в coverage_sequence: \n\n {coverage_sequence} \n\n"},
            ]
    )
    return response['choices'][0]['message']['content']


for i in range(start_test, end_test + 1):
    print(f"========== {i} ===========")
    file_name = f"my_dataset/{i}.json"

    os.makedirs(f"res_dataset/{i}/", exist_ok=True)

    with open(file_name, 'r') as file:
        parsed_data = json.load(file)
        method = parsed_data['method']
        coverage_sequences = parsed_data['tests']

        print("method")
        print(method)
        print()

        num_j_tests = len(coverage_sequences)

        for j in range(num_j_tests):
            file_name_2 = f"res_dataset/{i}/{i}_{j}.json"
            coverage_sequence = coverage_sequences[j]['coverage_sequence']

            print(f"coverage_sequence {j}")
            print(coverage_sequence)
            print()

            res = f(method, coverage_sequence)
            print(res)
            print()

    
            with open(file_name_2, 'w') as fi:
                json.dump({"result": res}, fi, indent=4)


