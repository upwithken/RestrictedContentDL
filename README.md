<h1 align="center">Restricted Content Downloader Telegram Bot</h1>

<p align="center">
  <a href="https://github.com/bisnuray/RestrictedContentDL/stargazers"><img src="https://img.shields.io/github/stars/bisnuray/RestrictedContentDL?color=blue&style=flat" alt="GitHub Repo stars"></a>
  <a href="https://github.com/bisnuray/RestrictedContentDL/issues"><img src="https://img.shields.io/github/issues/bisnuray/RestrictedContentDL" alt="GitHub issues"></a>
  <a href="https://github.com/bisnuray/RestrictedContentDL/pulls"><img src="https://img.shields.io/github/issues-pr/bisnuray/RestrictedContentDL" alt="GitHub pull requests"></a>
  <a href="https://github.com/bisnuray/RestrictedContentDL/graphs/contributors"><img src="https://img.shields.io/github/contributors/bisnuray/RestrictedContentDL?style=flat" alt="GitHub contributors"></a>
  <a href="https://github.com/bisnuray/RestrictedContentDL/network/members"><img src="https://img.shields.io/github/forks/bisnuray/RestrictedContentDL?style=flat" alt="GitHub forks"></a>
</p>

<p align="center">
  <em>Restricted Content Downloader: An advanced Telegram bot script to download restricted content such as photos, videos, audio files, or documents from Telegram private chats or channels. This bot can also copy text messages from Telegram posts.</em>
</p>
<hr>

## Features

- 📥 Download media (photos, videos, audio, documents).
- ✅ Supports downloading from both single media posts and media groups.
- 🔄 Progress bar showing real-time downloading progress.
- ✍️ Copy text messages or captions from Telegram posts.

## Requirements

Before you begin, ensure you have met the following requirements:

- Docker and Docker Compose installed on your system
- A Telegram bot token (you can get one from [@BotFather](https://t.me/BotFather) on Telegram)
- API ID and Hash: You can get these by creating an application on [my.telegram.org](https://my.telegram.org)
- To Get `SESSION_STRING` Open [@SmartUtilBot](https://t.me/SmartUtilBot). Bot and use /pyro command and then follow all instructions

> **Note**: All dependencies including Python, `pyrofork`, `pyleaves`, `tgcrypto`, and `ffmpeg` are automatically installed when you deploy with Docker Compose.

## Configuration

1. Open the `config.env` file in your favorite text editor.
2. Replace the placeholders for `API_ID`, `API_HASH`, `SESSION_STRING`, and `BOT_TOKEN` with your actual values:
   - **`API_ID`**: Your API ID from [my.telegram.org](https://my.telegram.org).
   - **`API_HASH`**: Your API Hash from [my.telegram.org](https://my.telegram.org).
   - **`SESSION_STRING`**: The session string generated using [@SmartUtilBot](https://t.me/SmartUtilBot).
   - **`BOT_TOKEN`**: The token you obtained from [@BotFather](https://t.me/BotFather).

3. Optional performance settings (add to `config.py`):
   - **`MAX_CONCURRENT_DOWNLOADS`**: Number of simultaneous downloads (default: 3)
   - **`BATCH_SIZE`**: Number of posts to process in parallel during batch downloads (default: 10)
   - **`FLOOD_WAIT_DELAY`**: Delay in seconds between batch groups to avoid flood limits (default: 3)

## Deploy the Bot

1. Clone the repository:
   ```sh
   git clone https://github.com/bisnuray/RestrictedContentDL
   cd RestrictedContentDL
   ```

2. Start the bot:
   ```sh
   docker compose up --build --remove-orphans
   ```

The bot will run in a containerized environment with all dependencies (Python, libraries, FFmpeg) automatically installed and managed.

To stop the bot:

```sh
docker compose down
```

## Deploy on Railway

Railway is a cloud platform that makes it easy to deploy applications. Follow these steps to deploy your bot on Railway:

### Prerequisites

1. A [Railway](https://railway.app) account (free tier available)
2. A GitHub account (to connect your repository)
3. Your Telegram bot credentials (same as above)

### Deployment Steps

1. **Push your code to GitHub** (if not already done):
   ```sh
   git add .
   git commit -m "Prepare for Railway deployment"
   git push origin main
   ```

2. **Create a new Railway project**:
   - Go to [Railway Dashboard](https://railway.app/dashboard)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Configure Environment Variables**:
   - In your Railway project dashboard, go to the "Variables" tab
   - Add the following environment variables:
     - `API_ID` - Your Telegram API ID
     - `API_HASH` - Your Telegram API Hash
     - `BOT_TOKEN` - Your bot token from @BotFather
     - `SESSION_STRING` - Your session string from @SmartUtilBot
     - `MAX_CONCURRENT_DOWNLOADS` (optional, default: 3)
     - `BATCH_SIZE` (optional, default: 10)
     - `FLOOD_WAIT_DELAY` (optional, default: 3)

4. **Deploy**:
   - Railway will automatically detect your `Dockerfile` and start building
   - The deployment will begin automatically
   - Check the "Deployments" tab for build logs

5. **Monitor your bot**:
   - View logs in the Railway dashboard
   - Your bot will automatically restart if it crashes
   - Check `/start` command in Telegram to verify it's running

### Important Notes for Railway

- **No persistent storage**: Railway uses ephemeral storage. Session files won't persist, but using `SESSION_STRING` (which this bot does) works perfectly.
- **Auto-restart**: The bot will automatically restart on failures.
- **Environment variables**: Always set sensitive data as environment variables in Railway, never commit them to your repository.
- **Logs**: Access real-time logs directly from the Railway dashboard.

## Usage

- **`/start`** – Welcomes you and gives a brief introduction.  
- **`/help`** – Shows detailed instructions and examples.  
- **`/dl <post_URL>`** or simply paste a Telegram post link – Fetch photos, videos, audio, or documents from that post.  
- **`/bdl <start_link> <end_link>`** – Batch-download a range of posts in one go.  

  > 💡 Example: `/bdl https://t.me/mychannel/100 https://t.me/mychannel/120`  
- **`/killall`** – Cancel any pending downloads if the bot hangs.  
- **`/logs`** – Download the bot’s logs file.  
- **`/stats`** – View current status (uptime, disk, memory, network, CPU, etc.).  

> **Note:** Make sure that your user session is a member of the source chat or channel before downloading.

## Author

- Name: Bisnu Ray
- Telegram: [@itsSmartDev](https://t.me/itsSmartDev)

> **Note**: If you found this repo helpful, please fork and star it. Also, feel free to share with proper credit!