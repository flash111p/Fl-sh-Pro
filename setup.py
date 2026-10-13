import os

# Create directory structure
os.makedirs("flash-pro/public", exist_ok=True)
os.makedirs("flash-pro/api", exist_ok=True)

# 1. index.html
with open("flash-pro/index.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flâsh Pro - All-in-One AI & Media Suite</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header class="navbar">
        <div class="logo">
            <i class="fa-solid fa-bolt-lightning"></i> Flâsh Pro
        </div>
        <nav class="nav-links">
            <a href="index.html" class="active">Home</a>
            <a href="ai-chat.html">AI Chat</a>
            <a href="ai-photo.html">AI Photo</a>
            <a href="downloader.html">Downloader</a>
        </nav>
    </header>
    <main class="hero">
        <div class="hero-badge">Next-Gen Web Suite</div>
        <h1>Welcome to <span class="gradient-text">Flâsh Pro</span></h1>
        <p>Your ultimate platform powered by advanced AI and lightning-fast media tools.</p>
        <div class="features-grid">
            <div class="feature-card" onclick="location.href='ai-chat.html'">
                <div class="icon-box chat-icon"><i class="fa-solid fa-comments"></i></div>
                <h3>AI Assistant Chat</h3>
                <p>Engage in smart conversations with our AI model.</p>
                <span class="link-text">Launch Chat <i class="fa-solid fa-arrow-right"></i></span>
            </div>
            <div class="feature-card" onclick="location.href='ai-photo.html'">
                <div class="icon-box photo-icon"><i class="fa-solid fa-wand-magic-sparkles"></i></div>
                <h3>AI Photo Generator</h3>
                <p>Transform your text prompts into stunning artworks.</p>
                <span class="link-text">Generate Art <i class="fa-solid fa-arrow-right"></i></span>
            </div>
            <div class="feature-card" onclick="location.href='downloader.html'">
                <div class="icon-box download-icon"><i class="fa-solid fa-cloud-arrow-down"></i></div>
                <h3>Universal Downloader</h3>
                <p>Download HD videos from TikTok, YouTube, and Facebook.</p>
                <span class="link-text">Start Downloading <i class="fa-solid fa-arrow-right"></i></span>
            </div>
        </div>
    </main>
    <footer>
        <p>&copy; 2026 Flâsh Pro. Built with Vercel Serverless.</p>
    </footer>
</body>
</html>""")

# 2. ai-chat.html
with open("flash-pro/ai-chat.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Chat - Flâsh Pro</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header class="navbar">
        <div class="logo" onclick="location.href='index.html'" style="cursor: pointer;"><i class="fa-solid fa-bolt-lightning"></i> Flâsh Pro</div>
        <nav class="nav-links">
            <a href="index.html">Home</a>
            <a href="ai-chat.html" class="active">AI Chat</a>
            <a href="ai-photo.html">AI Photo</a>
            <a href="downloader.html">Downloader</a>
        </nav>
    </header>
    <main class="chat-container">
        <div class="chat-header">
            <h2><i class="fa-solid fa-robot"></i> Flâsh AI Assistant</h2>
            <p>Ask anything, brainstorm ideas, or solve problems.</p>
        </div>
        <div class="chat-box" id="chatBox">
            <div class="message ai-message">
                <div class="msg-icon"><i class="fa-solid fa-bolt"></i></div>
                <div class="msg-content">Hello! I'm your Flâsh Pro AI assistant. How can I help you today?</div>
            </div>
        </div>
        <div class="chat-input-area">
            <input type="text" id="userInput" placeholder="Type your message here..." autocomplete="off">
            <button id="sendBtn"><i class="fa-solid fa-paper-plane"></i></button>
        </div>
    </main>
    <script>
        const chatBox = document.getElementById('chatBox');
        const userInput = document.getElementById('userInput');
        const sendBtn = document.getElementById('sendBtn');
        function appendMessage(sender, text) {
            const msgDiv = document.createElement('div');
            msgDiv.className = `message ${sender === 'user' ? 'user-message' : 'ai-message'}`;
            msgDiv.innerHTML = `<div class="msg-icon"><i class="fa-solid ${sender === 'user' ? 'fa-user' : 'fa-bolt'}"></i></div><div class="msg-content">${text}</div>`;
            chatBox.appendChild(msgDiv);
            chatBox.scrollTop = chatBox.scrollHeight;
        }
        sendBtn.addEventListener('click', () => {
            const text = userInput.value.trim();
            if(!text) return;
            appendMessage('user', text);
            userInput.value = '';
            setTimeout(() => appendMessage('ai', 'Flâsh Pro AI response simulation.'), 1000);
        });
    </script>
</body>
</html>""")

# 3. ai-photo.html
with open("flash-pro/ai-photo.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Photo Generator - Flâsh Pro</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header class="navbar">
        <div class="logo" onclick="location.href='index.html'" style="cursor: pointer;"><i class="fa-solid fa-bolt-lightning"></i> Flâsh Pro</div>
        <nav class="nav-links">
            <a href="index.html">Home</a>
            <a href="ai-chat.html">AI Chat</a>
            <a href="ai-photo.html" class="active">AI Photo</a>
            <a href="downloader.html">Downloader</a>
        </nav>
    </header>
    <main class="tool-container">
        <div class="tool-header">
            <h2><i class="fa-solid fa-wand-magic-sparkles"></i> AI Photo Generator</h2>
            <p>Describe your imagination and watch the AI bring it to life.</p>
        </div>
        <div class="generator-panel">
            <div class="prompt-box">
                <textarea id="imagePrompt" placeholder="Describe your image..."></textarea>
                <button id="generateBtn"><i class="fa-solid fa-sparkles"></i> Generate Image</button>
            </div>
            <div class="result-display" id="resultDisplay">
                <div class="placeholder-art"><i class="fa-regular fa-image"></i><p>Your generated artwork will appear here</p></div>
            </div>
        </div>
    </main>
    <script>
        document.getElementById('generateBtn').addEventListener('click', () => {
            const prompt = document.getElementById('imagePrompt').value;
            if(!prompt) return alert('Enter prompt!');
            document.getElementById('resultDisplay').innerHTML = '<div class="spinner-box"><i class="fa-solid fa-spinner fa-spin fa-3x"></i><p>Generating...</p></div>';
            setTimeout(() => {
                document.getElementById('resultDisplay').innerHTML = '<div class="image-output-card"><img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800" style="max-width:100%; border-radius:12px;"></div>';
            }, 1500);
        });
    </script>
</body>
</html>""")

# 4. downloader.html
with open("flash-pro/downloader.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Universal Video Downloader - Flâsh Pro</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header class="navbar">
        <div class="logo" onclick="location.href='index.html'" style="cursor: pointer;"><i class="fa-solid fa-bolt-lightning"></i> Flâsh Pro</div>
        <nav class="nav-links">
            <a href="index.html">Home</a>
            <a href="ai-chat.html">AI Chat</a>
            <a href="ai-photo.html">AI Photo</a>
            <a href="downloader.html" class="active">Downloader</a>
        </nav>
    </header>
    <main class="tool-container">
        <div class="tool-header">
            <h2><i class="fa-solid fa-cloud-arrow-down"></i> Universal Video Downloader</h2>
            <p>Paste link from TikTok, YouTube, or Facebook.</p>
        </div>
        <div class="downloader-panel">
            <div class="platform-badges">
                <span class="badge tiktok"><i class="fa-brands fa-tiktok"></i> TikTok</span>
                <span class="badge youtube"><i class="fa-brands fa-youtube"></i> YouTube</span>
                <span class="badge facebook"><i class="fa-brands fa-facebook"></i> Facebook</span>
            </div>
            <div class="input-group">
                <input type="text" id="videoUrl" placeholder="Paste video link here...">
                <button id="fetchBtn"><i class="fa-solid fa-magnifying-glass"></i> Fetch</button>
            </div>
            <div class="download-result" id="downloadResult">
                <div class="placeholder-art"><i class="fa-solid fa-video"></i><p>Enter video link above</p></div>
            </div>
        </div>
    </main>
    <script>
        document.getElementById('fetchBtn').addEventListener('click', async () => {
            const url = document.getElementById('videoUrl').value;
            if(!url) return alert('Enter URL!');
            const res = document.getElementById('downloadResult');
            res.innerHTML = '<div class="spinner-box"><i class="fa-solid fa-spinner fa-spin fa-3x"></i><p>Fetching...</p></div>';
            setTimeout(() => {
                res.innerHTML = '<div class="video-info-card"><h3>Video Ready</h3><a href="#" class="btn-primary" onclick="alert(\'Downloading...\')">Download MP4</a></div>';
            }, 1000);
        });
    </script>
</body>
</html>""")

# 5. style.css
with open("flash-pro/style.css", "w", encoding="utf-8") as f:
    f.write("""* { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Plus Jakarta Sans', sans-serif; }
body { background-color: #0b0f19; color: #f3f4f6; min-height: 100vh; display: flex; flex-direction: column; }
.navbar { display: flex; justify-content: space-between; align-items: center; padding: 20px 8%; background: rgba(15, 23, 42, 0.8); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(255, 255, 255, 0.08); position: sticky; top: 0; z-index: 1000; }
.logo { font-size: 1.5rem; font-weight: 800; color: #ffffff; display: flex; align-items: center; gap: 10px; }
.logo i { color: #f59e0b; }
.nav-links { display: flex; gap: 30px; }
.nav-links a { text-decoration: none; color: #94a3b8; font-weight: 600; transition: color 0.3s; }
.nav-links a:hover, .nav-links a.active { color: #f59e0b; }
.hero { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 60px 20px; max-width: 1100px; margin: 0 auto; }
.hero-badge { background: rgba(245, 158, 11, 0.1); color: #f59e0b; padding: 6px 16px; border-radius: 50px; font-size: 0.85rem; font-weight: 700; margin-bottom: 20px; border: 1px solid rgba(245, 158, 11, 0.2); }
.hero h1 { font-size: 3.5rem; font-weight: 800; margin-bottom: 20px; line-height: 1.2; }
.gradient-text { background: linear-gradient(135deg, #f59e0b 0%, #ef4444 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.hero p { font-size: 1.15rem; color: #94a3b8; max-width: 700px; margin-bottom: 50px; }
.features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; width: 100%; }
.feature-card { background: rgba(30, 41, 59, 0.5); border: 1px solid rgba(255, 255, 255, 0.08); padding: 35px 25px; border-radius: 20px; text-align: left; cursor: pointer; transition: transform 0.3s, border-color 0.3s; }
.feature-card:hover { transform: translateY(-5px); border-color: #f59e0b; }
.icon-box { width: 55px; height: 55px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; margin-bottom: 20px; }
.chat-icon { background: rgba(59, 130, 246, 0.15); color: #3b82f6; }
.photo-icon { background: rgba(168, 85, 247, 0.15); color: #a855f7; }
.download-icon { background: rgba(16, 185, 129, 0.15); color: #10b981; }
.feature-card h3 { font-size: 1.3rem; margin-bottom: 10px; }
.feature-card p { font-size: 0.95rem; color: #94a3b8; margin-bottom: 20px; }
.link-text { font-size: 0.9rem; font-weight: 700; color: #f59e0b; display: flex; align-items: center; gap: 8px; }
.chat-container, .tool-container { max-width: 900px; margin: 40px auto; width: 90%; flex: 1; display: flex; flex-direction: column; }
.chat-header, .tool-header { margin-bottom: 25px; text-align: center; }
.chat-box { background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 20px; padding: 25px; flex: 1; min-height: 400px; max-height: 500px; overflow-y: auto; display: flex; flex-direction: column; gap: 20px; margin-bottom: 20px; }
.message { display: flex; gap: 15px; max-width: 80%; }
.ai-message { align-self: flex-start; }
.user-message { align-self: flex-end; flex-direction: row-reverse; }
.msg-icon { width: 40px; height: 40px; border-radius: 50%; background: #1e293b; display: flex; align-items: center; justify-content: center; color: #f59e0b; flex-shrink: 0; }
.user-message .msg-icon { background: #3b82f6; color: #fff; }
.msg-content { background: #1e293b; padding: 15px 20px; border-radius: 15px; font-size: 0.95rem; line-height: 1.5; }
.user-message .msg-content { background: #2563eb; color: white; }
.chat-input-area, .input-group { display: flex; gap: 12px; background: rgba(30, 41, 59, 0.7); padding: 10px; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.08); }
.chat-input-area input, .input-group input, .prompt-box textarea { flex: 1; background: transparent; border: none; outline: none; color: white; font-size: 1rem; padding: 0 15px; }
.prompt-box textarea { width: 100%; height: 120px; resize: none; padding: 15px; margin-bottom: 15px; border-radius: 12px; background: #1e293b; border: 1px solid rgba(255, 255, 255, 0.08); }
.chat-input-area button, .input-group button, .prompt-box button, .btn-primary { background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color: white; border: none; padding: 12px 25px; border-radius: 12px; font-weight: 700; cursor: pointer; display: flex; align-items: center; gap: 8px; }
.generator-panel, .downloader-panel { background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 20px; padding: 30px; }
.platform-badges { display: flex; gap: 15px; margin-bottom: 20px; }
.badge { padding: 6px 14px; border-radius: 8px; font-size: 0.85rem; font-weight: 600; display: flex; align-items: center; gap: 6px; }
.badge.tiktok { background: rgba(0,0,0,0.4); color: #fff; }
.badge.youtube { background: rgba(239, 68, 68, 0.15); color: #ef4444; }
.badge.facebook { background: rgba(59, 130, 246, 0.15); color: #3b82f6; }
.result-display, .download-result { margin-top: 25px; min-height: 250px; border: 2px dashed rgba(255, 255, 255, 0.1); border-radius: 16px; display: flex; align-items: center; justify-content: center; text-align: center; padding: 20px; }
.placeholder-art { color: #64748b; }
.placeholder-art i { font-size: 3rem; margin-bottom: 10px; }
footer { text-align: center; padding: 20px; color: #64748b; font-size: 0.85rem; border-top: 1px solid rgba(255, 255, 255, 0.05); }""")

# 6. api/download.js
with open("flash-pro/api/download.js", "w", encoding="utf-8") as f:
    f.write("""export default function handler(req, res) {
    const { url } = req.query;
    if (!url) return res.status(400).json({ error: 'URL required' });
    return res.status(200).json({ success: true, downloadUrl: '#' });
}""")

print("Flâsh Pro project files created successfully inside 'flash-pro' folder!")
