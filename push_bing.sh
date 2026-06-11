#!/bin/bash
# Bing 主动推送脚本
# 登录 https://www.bing.com/webmasters → 提交 sitemap 即可,无需 API

# Bing IndexNow 推送(可选,效果显著,Bing + Yandex + Naver + DuckDuckGo 都用)
API_KEY="YOUR_INDEXNOW_KEY"  # 在 Bing Webmaster Tools → IndexNow 申请

URLS=(
"https://fengliwei001.github.io/jirou-baike/"
"https://fengliwei001.github.io/jirou-baike/#/exercise/barbell-bench-press"
"https://fengliwei001.github.io/jirou-baike/#/exercise/incline-bench-press"
"https://fengliwei001.github.io/jirou-baike/#/exercise/decline-bench-press"
"https://fengliwei001.github.io/jirou-baike/#/exercise/dumbbell-bench-press"
"https://fengliwei001.github.io/jirou-baike/#/exercise/incline-dumbbell-press"
"https://fengliwei001.github.io/jirou-baike/#/exercise/flat-dumbbell-fly"
"https://fengliwei001.github.io/jirou-baike/#/exercise/incline-dumbbell-fly"
"https://fengliwei001.github.io/jirou-baike/#/exercise/floor-dumbbell-press"
"https://fengliwei001.github.io/jirou-baike/#/exercise/cable-crossover-high-low"
"https://fengliwei001.github.io/jirou-baike/#/exercise/cable-crossover-low-high"
"https://fengliwei001.github.io/jirou-baike/#/exercise/machine-fly"
"https://fengliwei001.github.io/jirou-baike/#/exercise/chest-press-machine"
"https://fengliwei001.github.io/jirou-baike/#/exercise/svend-press"
"https://fengliwei001.github.io/jirou-baike/#/exercise/push-up"
"https://fengliwei001.github.io/jirou-baike/#/exercise/incline-push-up"
"https://fengliwei001.github.io/jirou-baike/#/exercise/decline-push-up"
"https://fengliwei001.github.io/jirou-baike/#/exercise/wide-push-up"
"https://fengliwei001.github.io/jirou-baike/#/exercise/diamond-push-up"
"https://fengliwei001.github.io/jirou-baike/#/exercise/push-up-plus"
"https://fengliwei001.github.io/jirou-baike/#/exercise/dumbbell-pullover"
"https://fengliwei001.github.io/jirou-baike/#/exercise/chest-dip"
"https://fengliwei001.github.io/jirou-baike/#/exercise/band-chest-fly"
"https://fengliwei001.github.io/jirou-baike/#/category/%E6%9D%A0%E9%93%83"
"https://fengliwei001.github.io/jirou-baike/#/category/%E5%93%91%E9%93%83"
"https://fengliwei001.github.io/jirou-baike/#/category/%E5%99%A8%E6%A2%B0"
"https://fengliwei001.github.io/jirou-baike/#/category/%E7%BB%9A%E7%B4%A2"
"https://fengliwei001.github.io/jirou-baike/#/category/%E5%BE%92%E6%89%8B"
)

if [ "$API_KEY" = "YOUR_INDEXNOW_KEY" ]; then
  echo "⚠️  请先在脚本里填入 IndexNow API KEY"
  echo "申请:https://www.bing.com/indexsumbit/getapi"
  exit 1
fi

# 用 JSON 批量提交
JSON_BODY=$(printf '"%s",' "${URLS[@]}" | sed 's/,$//')
curl -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d "{\"host\":\"fengliwei001.github.io\",\"key\":\"$API_KEY\",\"urlList\":[$JSON_BODY]}" \
  | head -5
echo ""
echo "✅ 已推送 ${#URLS[@]} 个 URL 到 IndexNow(Bing/Yandex/Naver 自动索引)"
