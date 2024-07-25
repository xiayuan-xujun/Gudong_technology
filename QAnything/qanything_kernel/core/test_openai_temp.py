#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2024/7/18 14:04
# @Author: Xujun
import os
from openai import OpenAI

def test_api(messages, model="chatbot", max_tokens=500, temperature=0):
    # Vllm方式，需必须符合输入的格式，多余的不行。
    # base_url = os.getenv('OPENAI_API_URL', 'http://0.0.0.0:8081/v1')
    client = OpenAI(
            api_key='token-abc123',
            base_url='http://0.0.0.0:8081/v1'
        )

    chat_response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )
    output_data = {"output": chat_response.choices[0].message.content.strip()}
    return output_data


if __name__ == "__main__":
    messages0 = [
        {'role': 'user', 'content': '哪些人有网络工程师证书。'},    #, 'message_class': '1'
        {'role': 'assistant', 'content': '[{"person_name":"张三"}, {"person_name":"李四"}]'},
        {'role': 'user', 'content': '生成上述第一个人的简历。\n 提取上述句子涉及到的名字，多余的名字不用提取，只提取名字。结果用列表保存'}
    ]
    messages1 = [
        {'role': 'user', 'content': "你好，你是谁？"}
    ]
    params = {
        "messages": messages0,
        "temperature": 0,
        "top_p": 0,
        "max_tokens": 10000,
        "stream": False
    }

    print("messages:", messages0)
    # output_data = test_api(**params)
    for i in range(10):
        if i %2 == 0:
            output_data = test_api(messages0)
            print(output_data)
        else:
            output_data = test_api(messages0)
            print(output_data)