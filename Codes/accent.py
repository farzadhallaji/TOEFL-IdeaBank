import requests
import soundfile as sf


API_URL = "https://api-inference.huggingface.co/models/Jzuluaga/accent-id-commonaccent_ecapa"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

def convert_wav_to_flac(input_wav, output_flac):
    data, samplerate = sf.read(input_wav)
    sf.write(output_flac, data, samplerate)

# Convert .wav to .flac
input_wav = "../Blue/001/MyVoices/1.wav"
output_flac = "../Blue/001/MyVoices/1.flac"
convert_wav_to_flac(input_wav, output_flac)


output = query(output_flac)
print(output)
