import pyttsx3, speech_recognition

def listen() -> str:
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        audio = sr.listen(source)
        speech = ""

        try:
            speech = sr.recognize_google(audio)
        except Exception as e:
            print("Exception:", str(e))

        return speech.lower()


def speak(text) -> None:
    print(text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":

    speak("Setting things up. This may take a moment...")

    from patterns import *

    regions = sc.get_regions()
    print()
        
    while True:

        speak("Listening...")
        text = listen() 
        # text = input().lower()
        result = ""

        for region in regions:
            if region in text.split(" "):
                for pattern, function in INPUT_PATTERNS.items():
                    if pattern.match(text):
                        result = function(region)
                        break
                else:
                    result = sc.get_total_cases_region(region) + sc.get_total_deaths_region(region) + sc.get_total_recoveries_region(region) + sc.get_total_active_region(region)
            
        if text.find("update") != -1:
            result = "Data is being updated. This may take a moment..."
            sc.update_data()

        if result:
            speak(result)

        for pattern, func in EXIT_PATTERNS.items():
            if pattern.match(text):
                speak("Exiting... Thank you for using.")
                func()
