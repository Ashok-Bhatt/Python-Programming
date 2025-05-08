from gtts import gTTS

mytext="Hardest choices need strongest wills."
language="hi"
speech=gTTS(text=mytext,lang=language,slow=True)
speech.save("./IWThanos.mp3")