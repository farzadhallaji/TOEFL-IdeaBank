from gradio_client import Client
import gradio_client

client = Client("https://mispeech-ced-base.hf.space/--replicas/r2aw4/")
result = client.predict(gradio_client.file("../Blue/001/MyVoices/1.wav"),api_name="/predict")
print(result)
