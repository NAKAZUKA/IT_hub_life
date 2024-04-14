import os

import pyaudio
from vosk import Model, KaldiRecognizer

import Anime
import DATAS as dat
import main

RATE = 44100
MODEL = 'vosk-model-small-ru-0.4'  # "vosk-model-small-ru-0.22" - ru, vosk-model-small-en-us-0.15 - eu - vosk-model-en-us-0.42-gigaspeech

try:
    os.remove('test.wav')
except:
    pass
Anime.start('begin', bender='stop', voice=False)
main.main("привет ВСЕМ", 'begin', anal=False)
Anime.start('begin', bender='stop', voice=False)


def script(text):
    import Anime, text_to_speech
    # text_to_speech.synthesize('Дай подумать!')
    # Anime.start('begin')

    if "кто ты" in text.lower():
        main.main("привет, я твой интерактивный помощник Бендер, я помогу сориентироваться в коледже и расскажу что у нас тут есть. Приложи пожалуйста свой пропуск чтобы я понял кто ты", 'hi', anal=False)
    elif "приложил" in text.lower():
        main.main("вижу вижу, ты студент и пользуешься Айтихаб лайф, чем я могу тебе помочь?", 'question', anal=False)
    elif "мероприятия" in text.lower():
        main.main("ну смотри. Что-то ещё?", 'events', anal=False)
    elif "клубы" in text.lower():
        main.main("У нас есть следующие клубы Шахматисты, любители кино, фотографы, спортсмены по различным видам спорта и многие другие. Что-то ещё?", 'clubs', anal=False)
    elif "спасибо" in text.lower():
        main.main("Да не за что! не забудь добавить меня в телеграмме, там пообщаемся. вот Qr-код", 'QR', anal=False)

    elif text != '':
        main.main(text, 'begin')
        Anime.start('begin', bender='stop', voice=False)


def start():
    global MODEL, RATE
    model = Model(r"models/vosk/" + MODEL)  # полный путь к модели
    rec = KaldiRecognizer(model, 44100)
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=RATE,
        input=True,
        frames_per_buffer=RATE
    )
    stream.start_stream()

    res = ''
    new_res = ''
    # go_anime('HI', 'T')
    dat.STATUS = True
    while True:
        if not dat.STATUS:
            continue
        print('Listening...')
        data = stream.read(RATE)
        if len(data) == 0:
            break
        try:
            res = rec.Result() if rec.AcceptWaveform(data) else rec.PartialResult()
            res = res.replace("\n", '')
            res = res.strip()
            if "\"text\" : \"" in res:
                res = str(res).removesuffix('"}')
                res = str(res).removeprefix('{  "text" : "')

                if res != 'result':
                    print(res)
                    script(res)

        except Exception as e:
            print(e)


    # print(rec.FinalResult())

if __name__ == '__main__':
    start()