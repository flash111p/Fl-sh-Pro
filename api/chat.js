export default async function handler(req, res) {
    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Method not allowed' });
    }

    const { message } = req.body;
    const apiKey = process.env.GEMINI_API_KEY; // Vercel Variables ထဲက ခေါ်သုံးမည်

    if (!apiKey) {
        return res.status(500).json({ error: 'API key not configured in Vercel Variables' });
    }

    try {
        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                contents: [{ parts: [{ text: message }] }]
            })
        });

        const data = await response.json();
        const aiReply = data.candidates?.[0]?.content?.parts?.[0]?.text || "တောင်းပန်ပါတယ်၊ အဖြေထုတ်လို့ မရပါ။";

        return res.status(200).json({ reply: aiReply });
    } catch (err) {
        return res.status(500).json({ error: 'Failed to communicate with AI' });
    }
}
