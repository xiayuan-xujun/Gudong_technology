import os
import requests

url = "http://10.10.205.4:30850/api/local_doc_qa/upload_files"
folder_path = "./docs/text2"  # 文件所在文件夹，注意是文件夹！！
data = {
    "user_id": "zzp",
    # "kb_id": "KB6f36eee97fd046ea8f781bb271cfa9ab",
    # "kb_id": "KBf73d2e12ac8d4236bfdc8399ee5fbec4", # 将每个产品分成单独放在一个文件中
    # KBf73d2e12ac8d4236bfdc8399ee5fbec4
    # "kb_id": "KB18b34a5de81349f4a047b030a08c50b1",
    "kb_id": "KB1078e1efe2864aa18a3afbfcc4b5d4b4",
    "mode": "soft"
}

files = []
for root, dirs, file_names in os.walk(folder_path):
    for file_name in file_names:
        if file_name.endswith(".txt"):  # 这里只上传后缀是md的文件，请按需修改，支持类型：
            file_path = os.path.join(root, file_name)
            files.append(("files", open(file_path, "rb")))

response = requests.post(url, files=files, data=data)
print(response.json())

# {'code': 200, 'msg': 'success，后台正在飞速上传文件，请耐心等待', 'data': [{'file_id': 'b6a767e5201843d7a1ad1ef4e0303b26', 'file_name': '产品类别.docx', 'status': 'gray', 'bytes': 22160, 'timestamp': '202406031347'}]}
