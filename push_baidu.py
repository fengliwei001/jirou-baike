#!/usr/bin/env python3
"""
百度站长平台主动推送脚本
每天运行一次,把 28 个 URL 推送给百度,加速收录。

使用方法:
  1. 登录 https://ziyuan.baidu.com/
  2. 添加站点 fengliwei001.github.io (DNS 验证最稳)
  3. 进入"链接提交 > 主动推送(实时)" > 接口调用地址
  4. 复制 token 填到下面 SITE_TOKEN
  5. 终端运行: python3 push_baidu.py
"""
import urllib.request, urllib.parse, json, sys, datetime

SITE = "https://fengliwei001.github.io/jirou-baike"
TOKEN = "YOUR_BAIDU_PUSH_TOKEN"  # ← 在百度站长平台复制

# 28 个 URL(主页 + 22 动作详情 + 5 器械分类)
URLS = [
    "/",
    "/#/exercise/barbell-bench-press",
    "/#/exercise/incline-bench-press",
    "/#/exercise/decline-bench-press",
    "/#/exercise/dumbbell-bench-press",
    "/#/exercise/incline-dumbbell-press",
    "/#/exercise/flat-dumbbell-fly",
    "/#/exercise/incline-dumbbell-fly",
    "/#/exercise/floor-dumbbell-press",
    "/#/exercise/cable-crossover-high-low",
    "/#/exercise/cable-crossover-low-high",
    "/#/exercise/machine-fly",
    "/#/exercise/chest-press-machine",
    "/#/exercise/svend-press",
    "/#/exercise/push-up",
    "/#/exercise/incline-push-up",
    "/#/exercise/decline-push-up",
    "/#/exercise/wide-push-up",
    "/#/exercise/diamond-push-up",
    "/#/exercise/push-up-plus",
    "/#/exercise/dumbbell-pullover",
    "/#/exercise/chest-dip",
    "/#/exercise/band-chest-fly",
    "/#/category/杠铃",
    "/#/category/哑铃",
    "/#/category/器械",
    "/#/category/绳索",
    "/#/category/徒手",
]

def push():
    api = f"https://data.zz.baidu.com/urls?site={SITE}&token={TOKEN}"
    body = "\n".join(SITE + u for u in URLS).encode("utf-8")
    req = urllib.request.Request(api, data=body, method="POST")
    req.add_header("Content-Type", "text/plain")
    req.add_header("User-Agent", "curl/7.79.1")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            data = json.loads(r.read().decode("utf-8"))
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if data.get("success_realtime"):
                print(f"✅ [{now}] 成功推送 {data['success_realtime']} 条,剩余配额 {data.get('remain_realtime','?')}")
            else:
                print(f"❌ [{now}] 失败:{data}")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        print(f"❌ HTTP {e.code}: {body}")
    except Exception as e:
        print(f"❌ 异常:{e}")

if __name__ == "__main__":
    if TOKEN == "YOUR_BAIDU_PUSH_TOKEN":
        print("⚠️  请先在脚本里填入百度站长平台的 TOKEN\n")
        print("获取方法:百度站长平台 → 链接提交 → 主动推送(实时) → 接口调用地址中的 token= 后面那串")
        sys.exit(1)
    push()
