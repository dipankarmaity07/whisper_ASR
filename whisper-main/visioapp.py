import whisper

model = whisper.load_model("base")
result = model.transcribe("PTT-20230707-WA0003.opus")
# print(result)
print(result["text"])