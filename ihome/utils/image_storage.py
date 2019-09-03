# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth, put_data, etag
import qiniu.config

# 需要填写你的 Access Key 和 Secret Key
access_key = 'Nfm_PgE3okvbHNgqRCQdmJFkEx-PUii42xldgn9V'
secret_key = 'juQ7d6bKaJC-zAF4FSNLywo0gMf8rlyHZNu9HJhI'


def storage(file_data):
	"""
	上传文件到七牛
	:param file_data:
	:return:
	"""
	# 构建鉴权对象
	q = Auth(access_key, secret_key)

	# 要上传的空间
	bucket_name = 'ihome'


	# 生成上传 Token，可以指定过期时间等
	token = q.upload_token(bucket_name, None, 3600)

	ret, info = put_data(token, None, file_data)
	print(info)
	print("*"*15)
	print(ret)