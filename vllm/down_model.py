#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2024/7/25 0:03
# @Author: Xujun
from modelscope.hub.snapshot_download import snapshot_download

from modelscope import snapshot_download
# 下载Qwen2-0.5B模型
model_dir = snapshot_download('qwen/Qwen2-0.5B', cache_dir='/model_base/model_hub')

# 下载bce-embedding和bce-reanker模型
model_dir2 = snapshot_download('netease-youdao/bce-embedding-base_v1', cache_dir='/model_base/model_hub')
model_dir3 = snapshot_download('netease-youdao/bce-reranker-base_v1', cache_dir='/model_base/model_hub')
