import pandas as pd
import os
import assemblyai as aai
import csv

# assign directory
directory = 'ToDo'
aai.settings.api_key = ""

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):

        transcriber = aai.Transcriber()

        audio_url = (
            f
        )

        config = aai.TranscriptionConfig(speaker_labels=True)

        transcript = transcriber.transcribe(audio_url, config)

        if f == "NotDone/.DS_Store":
            continue
        
        curr = ""
        for utterance in transcript.utterances:
            curr += f"Speaker {utterance.speaker}: {utterance.text}"

    with open('transcriptions.csv', 'a') as file:
         writer = csv.writer(file)
         writer.writerow(["name", "name", f, curr])
