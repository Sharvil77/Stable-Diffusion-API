from fastapi import FastAPI
from fastapi.responses import FileResponse
from scipy.io import wavfile
from scipy.io.wavfile import write as write_wav
from bark import SAMPLE_RATE, generate_audio, preload_models

app = FastAPI()

@app.post("/getAudio")
def post_getaudio(text_prompt: str):
    # download and load all models
    preload_models()

    # generate audio from text
    audio_array = generate_audio(text_prompt)

    # save & return the audio array as out_audio.wav file
    write_wav("./out_audio.wav", SAMPLE_RATE, audio_array)
    return FileResponse("./out_audio.wav")