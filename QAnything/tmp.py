import os

import pandas as pd
path = "./docs/docx/16N产品匹配结果v1.xlsx"

df = pd.read_excel(path)
df = df.fillna("")
df_list = df.to_dict("records")
data_dir = "./docs/text4"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)


for i,line in enumerate(df_list):
    with open(f"{data_dir}/产品{i}.txt", 'w', encoding="utf-8") as wfile:
        #wfile.writelines(f"###产品类别{i}:{line['产品类别']}\n")
        wfile.writelines(f"##产品名:{line['产品名']}\n")
        wfile.writelines(f"###{line['产品名']}适用的场景:{line['适用场景']}\n")
        wfile.writelines(f"##产品内容:{line['产品内容']}\n\n\n")
