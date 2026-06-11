# 肌肉百科 jirou-baike

中文健身动作库 · 22 个经典胸肌训练 · GIF 动态示范 + YouTube 视频教程

🌐 **线上地址:** https://fengliwei001.github.io/jirou-baike/

## 🔍 国内 SEO 收录清单(让百度/搜狗/360 找到你)

部署完 24-48 小时后,按以下顺序主动推送,加速收录:

### 1. 百度站长平台(最重要)
- 访问 https://ziyuan.baidu.com/
- 用百度账号登录,添加站点: `fengliwei001.github.io`
- 验证方式选 **CNAME** 或 **HTML 标签**(gh pages 不支持文件验证只能用 CNAME)
- 进入 **链接提交 → sitemap** 提交: `https://fengliwei001.github.io/jirou-baike/sitemap.xml`
- 进入 **链接提交 → 主动推送(实时)**,把 Python/curl 推送脚本复制下来每天跑一次

### 2. Bing Webmaster(微软搜索,被很多人忽略)
- https://www.bing.com/webmasters
- 添加并验证站点
- 提交 sitemap

### 3. 搜狗搜索站长平台
- https://zhanzhang.sogou.com/
- 添加站点 + 提交 sitemap

### 4. 360 搜索站长平台
- https://zhanzhang.so.com/
- 添加站点

### 5. 头条搜索(字节)
- https://zhanzhang.toutiao.com/
- 添加站点

### 6. 微信搜索(腾讯搜一搜)
- https://search.weixin.qq.com/
- 微信内搜索更看重 H5 体验和备案,gh pages 没备案收录慢但可以做

## 📢 站外引流建议(零成本)

- **小红书/抖音/B 站** 发"用肌肉百科学卧推"短视频,挂网站链接
- **知乎** 在"胸肌训练"问题下答长文,文末附链接
- **健身 QQ 群/微信群** 分享
- **即刻/微博** 分享

## 🚀 后续怎么更新

```bash
cd ~/Desktop/musclewiki-zh
# 改完文件后
git add -A
git commit -m "改了什么"
git push
# 1-2 分钟后 https://fengliwei001.github.io/jirou-baike/ 自动更新
```

## 🛠 后续可扩展

- [ ] 加入更多部位(背/肩/腿/臂/核心)
- [ ] 训练计划生成器(根据目标生成周计划)
- [ ] 接入百度统计看流量来源
- [ ] 自定义域名(有了域名可绑 `chest.yourdomain.com`)
