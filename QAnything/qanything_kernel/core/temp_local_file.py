#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2024/7/16 16:56
# @Author: Xujun
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
import re
from typing import List
from docx import Document


text_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", "。", "!", "！", "?", "？", "；", ";", "……", "…", "、", "，", ",", " ", ""],    # 可选参数，用于指定优先使用的分隔符，例如空格、句号等
    chunk_size=800,          # 分割文本的平均大小
    chunk_overlap=200,       # 允许的文本片段大小范围
    length_function=len,    # 长度计量方式，默认是按字符数
)

class ChineseTextSplitter(CharacterTextSplitter):
    def __init__(self, pdf: bool = False, sentence_size: int = 100, **kwargs):
        super().__init__(**kwargs)
        self.pdf = pdf
        self.sentence_size = sentence_size

    def split_text1(self, text: str) -> List[str]:
        if self.pdf:
            text = re.sub(r"\n{3,}", "\n", text)
            text = re.sub('\s', ' ', text)
            text = text.replace("\n\n", "")
        sent_sep_pattern = re.compile('([﹒﹔﹖﹗．。！？]["’”」』]{0,2}|(?=["‘“「『]{1,2}|$))')  # del ：；
        sent_list = []
        for ele in sent_sep_pattern.split(text):
            if sent_sep_pattern.match(ele) and sent_list:
                sent_list[-1] += ele
            elif ele:
                sent_list.append(ele)
        return sent_list

    def split_text(self, text: str) -> List[str]:   ##此处需要进一步优化逻辑
        if self.pdf:
            text = re.sub(r"\n{3,}", r"\n", text)
            text = re.sub('\s', " ", text)
            text = re.sub("\n\n", "", text)

        text = re.sub(r'([;；.!?。！？\?])([^”’])', r"\1\n\2", text)  # 单字符断句符
        text = re.sub(r'(\.{6})([^"’”」』])', r"\1\n\2", text)  # 英文省略号
        text = re.sub(r'(\…{2})([^"’”」』])', r"\1\n\2", text)  # 中文省略号
        text = re.sub(r'([;；!?。！？\?]["’”」』]{0,2})([^;；!?，。！？\?])', r'\1\n\2', text)
        # 如果双引号前有终止符，那么双引号才是句子的终点，把分句符\n放到双引号后，注意前面的几句都小心保留了双引号
        text = text.rstrip()  # 段尾如果有多余的\n就去掉它
        # 很多规则中会考虑分号;，但是这里我把它忽略不计，破折号、英文双引号等同样忽略，需要的再做些简单调整即可。
        ls = [i for i in text.split("\n") if i]
        for ele in ls:
            if len(ele) > self.sentence_size:
                ele1 = re.sub(r'([,，.]["’”」』]{0,2})([^,，.])', r'\1\n\2', ele)
                ele1_ls = ele1.split("\n")
                for ele_ele1 in ele1_ls:
                    if len(ele_ele1) > self.sentence_size:
                        ele_ele2 = re.sub(r'([\n]{1,}| {2,}["’”」』]{0,2})([^\s])', r'\1\n\2', ele_ele1)
                        ele2_ls = ele_ele2.split("\n")
                        for ele_ele2 in ele2_ls:
                            if len(ele_ele2) > self.sentence_size:
                                ele_ele3 = re.sub('( ["’”」』]{0,2})([^ ])', r'\1\n\2', ele_ele2)
                                ele2_id = ele2_ls.index(ele_ele2)
                                ele2_ls = ele2_ls[:ele2_id] + [i for i in ele_ele3.split("\n") if i] + ele2_ls[
                                                                                                       ele2_id + 1:]
                        ele_id = ele1_ls.index(ele_ele1)
                        ele1_ls = ele1_ls[:ele_id] + [i for i in ele2_ls if i] + ele1_ls[ele_id + 1:]

                id = ls.index(ele)
                ls = ls[:id] + [i for i in ele1_ls if i] + ls[id + 1:]
        return ls

file_path = r'/home/deeplearn/workspace/wxj/QAnything_old/docs/docx/财政部关于促进政府采购公平竞争优化营商环境的通知.docx'
loader = UnstructuredWordDocumentLoader(file_path)
texts_splitter = ChineseTextSplitter(pdf=False, sentence_size=100)
docs = loader.load_and_split(texts_splitter)

if not file_path.lower().endswith(".csv") and not file_path.lower().endswith(
        ".xlsx") and not file_path == 'FAQ':
    new_docs = []
    min_length = 200
    for doc in docs:
        if not new_docs:
            new_docs.append(doc)
        else:
            last_doc = new_docs[-1]
            if len(last_doc.page_content) + len(doc.page_content) < min_length:
                last_doc.page_content += '\n' + doc.page_content
            else:
                new_docs.append(doc)
    #
    docs = text_splitter.split_documents(new_docs)
# docs = new_docs
# 这里给每个docs片段的metadata里注入file_id
new_docs = []
for idx, doc in enumerate(docs):
    page_content = re.sub(r'[\n\t]+', '\n', doc.page_content).strip()
    new_doc = Document(page_content=page_content)
    new_doc.metadata["user_id"] = user_id
    new_doc.metadata["kb_id"] = kb_id
    new_doc.metadata["file_id"] = file_id
    new_doc.metadata["file_name"] = self.url if self.url else self.file_name
    new_doc.metadata["chunk_id"] = idx
    new_doc.metadata["file_path"] = self.file_path
    if 'faq_dict' not in doc.metadata:
        new_doc.metadata['faq_dict'] = {}
    else:
        new_doc.metadata['faq_dict'] = doc.metadata['faq_dict']
    new_docs.append(new_doc)


def split_second_level_docs(docs):
    pass