# todolist
- [ ] chatGPT-4境内外比对验证
- [ ] sparse & human reward evaluation
- [ ] 多大模型组合
- [ ] 大模型过滤规则的制订和试验
- [ ] 
- [ ] 


# 使用中出现的问题和解决方法
- openai境内代理的问题
    - 使用文件proxy/proxy.py中的get_openai_response进行替代
    - 这个是将openai的调用使用代理给的访问地址进行转发
- 联网问题
    - 遇到服务器无法ping通外网的问题
    - 解决方法：将proxy/openaiServer.py放到可以连接外网的电脑上
    - 修改为对应电脑上的ip和端口，`python openaiServer.py`即可运行。
    - 将上述ip和端口放到proxy/proxy.py中，即可完成跳转
- 多gpu和单卡使用的问题
    - 在cfg/config.py文件中添加visible_gpus: [0,1] 
    - 注意它的意义是否尽可能使用多块GPU，只接受两个值，长度是小于等于1（用一个gpu），还是大于1（用所有gpu）
- eureka使用过程中cuda会out-of-memory的问题
    - 也做了相应的修改