# 環境建置

## 建立自己的伺服器

建立 Discord 帳號並登入後，選左邊一欄的 + 號(新增一個伺服器) -> 建立自己的 -> 我和我的好友 -> 設定伺服器名稱 -> 建立

這樣伺服器便建立完成

## 建立新應用程式(New Application)

進到 [Devopler Protal](https://discord.com/developers/applications)，案右上方的 New Application -> 幫自己的應用程式取名。

進入剛建立的機器人，進入左側選單的設定，分別為 OAuth2 和 Bot

### OAuth2 頁面
1. 按下 Reset Secret 產生新的 Cilent Secret(記錄下來)
2. SCOPES 區塊選擇 bot
3. BOT PERMISSIONS 區塊勾選 Administrator

以上的步驟做完，最下方的 Generated URL 的區塊會產生一個網址，此時開新分頁連線該網址完成授權。

## bot 頁面

找到 Privileged Gateway Intents 將以下三個選項都開啟：

1. Presence Intent
2. Server Members Intent
3. Message Content Intent

按下 Save Changes 儲存變動

## 啟動 Discord Bot

### 在 github 上建立一個 discord_bot 的 repo，clone 到 linux 機器上

```bash
python3 clone https://github.com/monesijd/discord_bot.git
```

### 建立 venv 環境

```bash
python3 -m venv .venv
```

### 進入 venv 環境

```bash
source .venv/bin/activate
```

### 安裝相關套件
```bash
pip install pip setuptools wheel -U
pip install discord
```

### 設置環境變數，啟動程式碼
```bash
export DISCORD_BOT_TOKEN=<填入上面步驟產生的 CLIENT SECRET>
# 等號兩邊不能有空白
python3 bot.py
```

### 離開 venv
```bash
deactivate
```
