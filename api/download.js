export default function handler(req, res) {
    const { url } = req.query;

    if (!url) {
        return res.status(400).json({ error: 'Video URL is required' });
    }

    let platform = 'Unknown';
    if (url.includes('tiktok.com')) platform = 'TikTok';
    else if (url.includes('youtube.com') || url.includes('youtu.be')) platform = 'YouTube';
    else if (url.includes('facebook.com') || url.includes('fb.watch')) platform = 'Facebook';

    // In production, integrate actual scraping or third-party download API here
    return res.status(200).json({
        success: true,
        platform: platform,
        title: `Fetched Video from ${platform}`,
        downloadUrl: '#',
        thumbnail: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=300&auto=format&fit=crop'
    });
}
