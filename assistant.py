import pyttsx3, speech_recognition

from scraper import Scraper
from patterns import TOTAL_PATTERNS, REGION_PATTERNS, EXIT_PATTERNS

def listen() -> str:
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        audio = sr.listen(source)
        speech = ""

        try:
            speech = sr.recognize_google(audio)
        except Exception as e:
            print("Exception: ", str(e))

        return speech.lower()


def speak(text) -> None:
    print(text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    speak("Setting things up. This may take a moment...")
    sc = Scraper()
    regions = sc.get_regions()
    print()

    while True:

        speak("Listening...")
        text = print(listen())
        # text = input().lower()
        result = ""

        for word in text.split():
            if word in regions:
                for pattern, function in REGION_PATTERNS.items():
                    if pattern.match(text):
                        result = function(sc, word)
                if not result:
                    result = ( sc.get_total_cases_region(word) 
                    + sc.get_total_deaths_region(word) 
                    + sc.get_total_recoveries_region(word) 
                    + sc.get_total_active_region(word)
                    )
                break
        else:
            for pattern, function in TOTAL_PATTERNS.items():
                if pattern.match(text):
                    result = function(sc)
                    break;

        if text.find("update") != -1:
            result = "Data is being updated. This may take a moment..."
            sc.update_data()

        if result:
            speak(result)

        for pattern, func in EXIT_PATTERNS.items():
            if pattern.match(text):
                speak("Exiting... Thank you for using this app.")
                func()
