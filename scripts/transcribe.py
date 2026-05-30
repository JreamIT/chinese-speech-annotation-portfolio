import whisper
from pathlib import Path

model = whisper.load_model("base")

audio_dir = Path("audio")
output_dir = Path("model_transcripts")
output_dir.mkdir(exist_ok=True)

for audio_file in audio_dir.glob("*"):
    if audio_file.suffix.lower() not in [".mp3", ".wav", ".m4a"]:
        continue

    result = model.transcribe(str(audio_file), language="zh")
    output_path = output_dir / f"{audio_file.stem}.txt"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result["text"])

    print(f"Done: {audio_file.name}")