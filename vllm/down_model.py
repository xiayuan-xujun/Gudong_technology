#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2024/7/25 0:03
# @Author: Xujun
from modelscope.hub.snapshot_download import snapshot_download

from modelscope import snapshot_download
model_dir = snapshot_download('qwen/Qwen2-0.5B', cache_dir='/model_base/model_hub')
