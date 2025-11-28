# Railway Deployment Setup Guide

This project is configured to work seamlessly with **both local development and Railway cloud hosting**.

## How It Works

The application uses a **dual-configuration approach**:

### 1. Local Development (Optional)
- Uses `config.env` file (if present)
- Loaded via `python-dotenv` library
- File is ignored by git (never committed)
- Perfect for testing on your computer

### 2. Railway Deployment (Primary)
- Uses environment variables set in Railway dashboard
- No file needed - Railway injects variables directly
- More secure and production-ready
- Works out of the box!

## Code Design

The `config.py` file is designed to work with both:

```python
# Tries to load config.env (for local dev) - fails gracefully if missing
try:
    load_dotenv("config.env")
except:
    pass  # Railway deployments don't need this file

# Reads from environment variables (works everywhere)
BOT_TOKEN = getenv("BOT_TOKEN")  # Works with config.env OR Railway env vars
```

**Result:** The same code works locally AND on Railway without any changes!

---

## Why This Design?

✅ **Upstream Compatible**: Works with original repo (expects config.env for local)  
✅ **Railway Ready**: Works with Railway environment variables  
✅ **No Breaking Changes**: Original dev's workflow still works  
✅ **Clean Separation**: Local secrets stay local, Railway secrets in Railway dashboard  

---

## Configuration Options

### Option A: Railway Only (Recommended for Production)

1. Deploy to Railway
2. Set environment variables in Railway dashboard:
   - `API_ID`
   - `API_HASH`
   - `BOT_TOKEN`
   - `SESSION_STRING`
3. No `config.env` file needed ✅

### Option B: Local Development (Optional)

1. Create `config.env` file locally:
   ```
   API_ID=your_id
   API_HASH=your_hash
   BOT_TOKEN=your_token
   SESSION_STRING=your_session
   ```
2. Run locally: `python3 main.py` or `docker compose up`
3. File stays on your computer (gitignored)

### Option C: Both (Development + Production)

- Use `config.env` for local testing
- Set environment variables in Railway for production
- Same code works in both places! ✅

---

## Railway Environment Variables

Set these in Railway dashboard → Variables tab:

### Required:
- `API_ID` - Your Telegram API ID (number)
- `API_HASH` - Your Telegram API Hash (string)
- `BOT_TOKEN` - Bot token from @BotFather (format: `123456:ABC...`)
- `SESSION_STRING` - Session string from @SmartUtilBot

### Optional (have defaults):
- `MAX_CONCURRENT_DOWNLOADS` - Default: `3`
- `BATCH_SIZE` - Default: `10`
- `FLOOD_WAIT_DELAY` - Default: `3`

---

## Upstream Sync Compatibility

When you pull updates from the original repo:

✅ **config.py changes**: The original dev might update it, but the logic stays compatible  
✅ **No conflicts expected**: Railway-specific comments don't break anything  
✅ **Local dev still works**: Original dev's config.env approach still works  
✅ **Railway still works**: Environment variable reading still works  

The changes are **additive** (added comments, better error messages) - nothing removed or changed in a breaking way.

---

## File Structure

```
RestrictedContentDL/
├── config.py          # Dual-mode: reads from config.env (local) OR env vars (Railway)
├── config.env         # Local dev only (gitignored, never committed)
├── Dockerfile         # Works for both local Docker AND Railway
├── railway.json       # Railway-specific config (won't affect local dev)
├── .dockerignore      # Optimizes Docker builds (works everywhere)
└── ...
```

---

## Troubleshooting

### "Error: BOT_TOKEN environment variable must be set"

**On Railway:**
- Go to Railway dashboard → Variables tab
- Add `BOT_TOKEN` environment variable
- Wait for auto-redeploy

**Local:**
- Create/update `config.env` file
- Add line: `BOT_TOKEN=your_token_here`
- Restart the bot

### "config.env not found" (Warning only)

- This is normal for Railway deployments
- The code handles this gracefully
- Railway uses environment variables instead
- **No action needed** ✅

### "How do I test locally before deploying?"

1. Create `config.env` with your credentials
2. Run: `python3 main.py` or `docker compose up`
3. Test your bot
4. Deploy to Railway (uses env vars, not config.env)

---

## Best Practices

1. **Never commit secrets** - `config.env` is gitignored ✅
2. **Use Railway env vars for production** - More secure ✅
3. **Test locally first** - Use `config.env` for quick testing ✅
4. **Sync with upstream safely** - Your Railway config won't break ✅

---

## Summary

- ✅ Works locally (with config.env)
- ✅ Works on Railway (with environment variables)
- ✅ Upstream compatible (original dev's workflow still works)
- ✅ No breaking changes (additive improvements only)
- ✅ Secure (secrets never committed)

**Your Railway deployment is ready to go!** 🚀

