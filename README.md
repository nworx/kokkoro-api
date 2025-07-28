# Kokoro TTS with FastAPI

This is a Text-to-Speech API using Kokoro and FastAPI.

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone [https://github.com/your-username/kokoro-tts-api.git](https://github.com/nworx/kokkoro-api.git)
cd kokkoro-api
```

### 2. Set up Virtual Environment

```bash
python3.11 -m venv kokoro_env_testing 
source kokoro_env_testing/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt 
```

### 4. Run the FastAPI App

```bash
python -m uvicorn textToSpeech:app --reload
```

### 5. Test the Endpoint

Open Postman:
```
POST http://127.0.0.1:8000/convert_text_to_speech/
Body:
{
  "text": "Hello and Hi , and welcome. This is a technical interview designed to help you prepare for real world product engineering interviews. During this session I will be asking you a series of coding or technical reasoning questions. As we go through the interview, I encourage you to think out loud approach problems methodically and be honest. if you are uncertain, that is completely okay. Try to treat this experience just like a real interview. If you are all set, can we begin?",
  "voiceName": "af_heart"
}
```

### Output:
Returns a WAV audio response.

---

## Notes

- Make sure to install `libsndfile` if `soundfile` throws errors.
- Torch may require CUDA (optional).

