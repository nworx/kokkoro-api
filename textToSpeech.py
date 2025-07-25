import spacy
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from io import BytesIO
from kokoro import KPipeline
import soundfile as sf
import torch


# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Initialize the FastAPI app
app = FastAPI()

# Initialize the KPipeline
pipeline = KPipeline(lang_code='a')

# Create a Pydantic model for the incoming request data
class TextRequest(BaseModel):
    text: str
    voiceName: str

# API endpoint to convert text to speech
@app.post("/convert_text_to_speech/")
async def convert_text_to_speech(request: TextRequest):
    text = request.text
    voiceName = request.voiceName
    try:
        # Use Kokoro pipeline to generate the audio
        generator = pipeline(text, voice=voiceName)
        for i, (gs, ps, audio) in enumerate(generator):
            # Save audio to a buffer (BytesIO)
            audio_buffer = BytesIO()
            sf.write(audio_buffer, audio, 24000, format='WAV')
            audio_buffer.seek(0)
            return StreamingResponse(audio_buffer, media_type="audio/wav")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating speech: {str(e)}")
