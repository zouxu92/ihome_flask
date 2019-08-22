# coding:utf-8

from . import api
from ihome.utils.captcha.captcha import captcha
from ihome import redis_store, constants
from flask import current_app, jsonify, make_response
from ihome.utils.response_code import RET

# GET 127.0.0.1/api/v1.0/image_codes/<image_code_id>

@api.route("/image_codes/<image_code_id>")
def get_imge_code(image_code_id):
	"""
	获取图片验证码
	:return:  正常：验证码图片 异常：返回json
	"""
	# 1.获取参数
	# 2.检验参数
	# 3.业务逻辑处理
	# 生成验证码图片
	# 名字， 真实文本， 图片数据
	name, text, image_data = captcha.generate_captcha()

	# 将验证码真实值与编号保存到redis中, 设置有效期
	# 单条维护记录，选用字符串 "image_code_编号1":"真实值"
	#redis_store.set("image_code_%s" % image_code_id, text)
	#redis_store.expire("image_code_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES)
	# 将上面的两条设置以及设置有效期一条语句进行
	try:
		redis_store.setex("image_code_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)
	except Exception as e:
		# 捕获异常， 记录日志
		current_app.logger.error(e)
		# return jsonify(errno=RET.DBERR, errmsg="save image code id failed")
		return jsonify(errno=RET.DBERR, errmsg="保存图片验证码失败")

	# 4.返回值
	resp = make_response(image_data)
	resp.headers["Content-Type"] = "image/jpg"
	return resp