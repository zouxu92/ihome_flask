# ihome_flask  爱家公寓

1. 主页
    1.1 最多5个房屋logo图片展示，点击可跳转至房屋详情页面
    1.2 提供登陆/注册入口，登陆后显示用户名，点击可跳转至个人中心
    1.3 用户可以选择城区、入住时间、离开时间等条件进行搜索
    1.4 城区的区域信息需动态加载

2. 注册
    2.1 用户账号默认为手机号
    2.2 图片验证码正确后才能发送短信验证码
    2.3 短信验证码每60秒可发送一次
    2.4 每个条件出错时有相应错误提示

3. 登陆
    3.1 用手机号与密码登陆
    3.2 错误时有相应提示

4. 房屋列表页
    4.1 可根据入住离开时间、区域进行筛选，并可进行排序
    4.2 房屋信息分页加载
    4.3 区域信息动态加载
    4.4 筛选条件更新后，页面立即刷新

5. 房屋详情页
    5.1 需展示的详细信息参考设计图
    5.2 提供预定入口
    5.3 若是房东本人查看房屋信息时，预定入口不显示

6. 房屋预定
    6.1 由用户确定入住时间
    6.2 根据用户确定的入住离开时间实时显示合计天数与总金额

7. 我的爱家
    7.1 显示个人头像、手机号、用户名（用户名未设置时为用户手机号）
    7.2 提供修改个人信息的入口
    7.3 提供作为房客下单的查询入口
    7.4 提供成为房东所需实名认证的入口
    7.5 提供作为房东发布房屋信息的入口
    7.6 提供作为房东查询客户订单的入口
    7.7 提供退出的入口

8. 个人信息修改
    8.1 可以修改个人头像
    8.2 可以修改用户名
    8.3 登陆手机号不能修改
    8.4 上传头像与用户名分开保存
    8.5 上传新头像后页面理解显示新头像

9. 我的订单（房客）
    9.1 按时间倒序显示订单信息
    9.2 订单完成后提供评价功能
    9.3 已评价的订单能看到评价信息
    9.4 被拒绝的订单能看到拒单原因

10. 实名认证
    10.1 实名认证只可进行一次
    10.2 提交认证信息后再次进入只能查看信息，不能修改
    10.3 认证信息包含姓名与身份证号

11. 我的房源
    11.1 未实名认证的用户不能发布新房源信息，需引导到实名认证页面
    11.2 按时间倒序显示已经发布的房屋信息
    11.3 点击房屋可以进入详情页面
    11.4 对实名认证的用户提供发布新房屋的入口

12. 发布新房源
    12.1 需要用户填写全部房屋信息
    12.2 房屋的文字信息与图片分开操作

13. 客户订单（房东）
    13.1 按时间倒序显示用户下的订单
    13.2 对于新订单提供接单与拒单的功能
    13.3 拒单必须填写拒单原因
    13.4 若客户进行了订单评价，需显示

14. 退出
    14.1 提供退出功能
