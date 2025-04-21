import random
import asyncio

async def analyze_audio(file):
    # Simulate a delay to mimic audio processing
    await asyncio.sleep(1)

    return {
        "filename": file.filename,
        "duration": f"{random.randint(1, 300)} seconds",
        "bitrate": f"{random.choice([128, 192, 256, 320])} kbps",
        "status": "success"
    }