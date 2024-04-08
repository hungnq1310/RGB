import requests
import sseclient # pip install sseclient-py

def api_inference(url, headers, data, verify=False, stream=True):
  stream_response = requests.post(url, headers=headers, json=data, verify=verify, stream=stream)
  client = sseclient.SSEClient(stream_response)
  return client

def format_prompt(prompt_class, kwargs):
    return prompt_class(**kwargs).get_example(
        is_training=False,
        do_generative_eval=True,
        task_type="CAUSAL_LM"
    )['prompt']