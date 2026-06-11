#!/usr/bin/env python3
"""
一键推送脚本:同时推送到百度 + IndexNow(Bing/Yandex/Naver)
每天跑一次,加速搜索引擎收录。

用法:
  python3 daily_push.py
"""
import urllib.request, urllib.parse, json, subprocess, sys, datetime, os

SITE = "https://fengliwei001.github.io/jirou-baike"
HOST = "fengliwei001.github.io"

URLS = [
    "/", "/#/exercise/barbell-bench-press", "/#/exercise/incline-bench-press",
    "/#/exercise/decline-bench-press", "/#/exercise/dumbbell-bench-press",
    "/#/exercise/incline-dumbbell-press", "/#/exercise/flat-dumbbell-fly",
    "/#/exercise/incline-dumbbell-fly", "/#/exercise/floor-dumbbell-press",
    "/#/exercise/cable-crossover-high-low", "/#/exercise/cable-crossover-low-high",
    "/#/exercise/machine-fly", "/#/exercise/chest-press-machine",
    "/#/exercise/svend-press", "/#/exercise/push-up", "/#/exercise/incline-push-up",
    "/#/exercise/decline-push-up", "/#/exercise/wide-push-up", "/#/exercise/diamond-push-up",
    "/#/exercise/push-up-plus", "/#/exercise/dumbbell-pullover", "/#/exercise/chest-dip",
    "/#/exercise/band-chest-fly",
    "/#/category/杠铃", "/#/category/哑铃", "/#/category/器械",
    "/#/category/绳索", "/#/category/徒手",
]

def push_baidu(token):
    if not token:
        print("⏭️  百度:跳过(未配置 token)")
        return
    api = f"https://data.zz.baidu.com/urls?site={SITE}&token={token}"
    body = "\n".join(SITE + u for u in URLS).encode("utf-8")
    req = urllib.request.Request(api, data=body, method="POST")
    req.add_header("Content-Type", "text/plain")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            data = json.loads(r.read().decode("utf-8"))
            n = data.get("success_realtime", 0)
            print(f"✅ 百度:推送 {n} 条,剩余 {data.get('remain_realtime','?')}")
    except Exception as e:
        print(f"❌ 百度:{e}")

def push_indexnow(api_key):
    if not api_key:
        print("⏭️  IndexNow:跳过(未配置 API key)")
        return
    full_urls = [SITE + u for u in URLS]
    payload = {"host": HOST, "key": api_key, "urlList": full_urls}
    req = urllib.request.Request("https://api.indexnow.org/indexnow",
                                  data=json.dumps(payload).encode("utf-8"),
                                  method="POST")
    req.add_header("Content-Type", "application/json; charset=utf-8")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            print(f"✅ IndexNow:HTTP {r.status} - 推送 {len(full_urls)} 条(Bing/Yandex/Naver/DuckDuckGo)")
    except urllib.error.HTTPError as e:
        print(f"❌ IndexNow:HTTP {e.code} - {e.read().decode()[:200]}")
    except Exception as e:
        print(f"❌ IndexNow:{e}")

if __name__ == "__main__":
    # 从环境变量读取(更安全,不入库)
    baidu_token = os.environ.get("BAIDU_PUSH_TOKEN", "")
    indexnow_key = os.environ.get("INDEXNOW_KEY", "")

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"🚀 [{now}] 开始推送 {len(URLS)} 个 URL")
    print(f"   站点:{SITE}\n")

    push_baidu(baidu_token)
    push_indexnow(indexnow_key)

    print("\n💡 提示:也可直接编辑 push_baidu.py 硬编码 token(简单但不安全)")
