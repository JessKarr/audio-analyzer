from fastapi import APIRouter, File, UploadFile
from app.audio_utils import analyze_audio

router = APIRouter()

@router.post("/analyze-audio/")
async def analyze_audio_endpoint(file: UploadFile = File(...)):
    result = await analyze_audio(file)
    return result