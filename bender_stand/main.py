# import RecFace as rf
import MyFunc as mf
import time

import Anime
import text_to_text as txt
# import Silero as sil
import text_to_speech as ts


def main(text, img, anal=True):
    print('question-answer system')
    if anal:
        text = txt.text_to_text(text)
    text = mf.pre_tokenizing(text)
    print('--- ' + text)
    #     # print('Silero system')
    #     # sil.start(result, voice='aidar', sample_rate=48000)
    print('text-to-voice system')
    ts.synthesize(text)
    # print('Tokenizing system')
    # tokens = vt.start()
    print('Anime system')
    # try:
    Anime.start(img, bender='voice', anal=anal)
    if anal:
        Anime.start('begin', bender='stop', voice=False)
    print("OK!!!")
# main('1')