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
    engine = pyttsx3.init()
    engine.say(text)
    print(text)
    engine.runAndWait()


def query(sc: Scraper, text: str, regions: list) -> str:
    for word in text.split():
        if word in regions:
            for pattern, function in REGION_PATTERNS.items():
                if pattern.match(text):
                    return function(sc, word)
            return (sc.get_total_cases_region(word)
                + sc.get_total_deaths_region(word)
                + sc.get_total_recoveries_region(word)
                + sc.get_total_active_region(word))

    for pattern, function in TOTAL_PATTERNS.items():
        if pattern.match(text):
            return function(sc)

    return "";


def main(sc: Scraper) -> None:
    regions = sc.get_regions()
    speak("")
    run = True

    while run:
        speak("Listening...")
        # text = print(listen())
        text = input().lower()
        result = query(sc, text, regions)

        if not result and text.find("update") != -1:
            result =  sc.update_data()
        elif not result and \
            any([pattern.match(text) for pattern in EXIT_PATTERNS]):
            run = False
            result = "Exiting... Have a good day!"

        speak(result)


if __name__ == "__main__":
    speak("Setting things up. This may take a moment...")

    try:
        sc = Scraper()
    except RuntimeError as e:
        print(f"\nException {e} ocurred.\n")
        speak("Unable to connect to network.")
        speak("Make sure you have a stable internet connection.")
    except Exception as e:
        speak("Unexpected error ocurred.")
        print("If the problem persists let me know by mail \
        aakashjainofficial@gmail.com.")
    else:
        main(sc)