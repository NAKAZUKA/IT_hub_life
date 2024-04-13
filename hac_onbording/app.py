from flask import Flask, render_template, request, send_file, send_from_directory
import MyFunc as mf

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/<string:strin>', methods = ['GET'])
def indexi(strin):
    ot = {}
    if request.method == 'GET':
        ot = dict(request.args)
        if ot != {}:
            print(ot)
    # ot['id'] = 1
    try:
        ot['id']
    except:
        ot['id'] = 1

    if strin == 'friends':
        ot = mf.Friends()
    if strin == 'rating':
        ot = mf.Rating()
    if strin == 'profile':
        ot = mf.Profile(ot['id'])#()
    if strin == 'clubs':
        ot = mf.Clubs()
    if strin == 'club_detail':
        ot = mf.Club_detail(ot['id'])
    if strin == 'events':
        ot = mf.Events()
    if strin == 'event_detail':
        ot = mf.Event_detail(ot['id'])
    if strin == 'quests':
        ot = mf.Quests()
    if strin == 'quest_detail':
        ot = mf.Quest_detail(ot['id'])
    if strin == 'library':
        try:
            ot = mf.Library(ot['path'], ot['file'], id=1)
        except:
            ot = mf.Library('', '', id=1)

    if strin == 'favicon.ico':
        return ''
    if strin == 'get_file':
        ott = mf.Library(ot['path'], ot['file'], id=1)
        return send_from_directory(ott + "/", ot['file'])

    print("\nOT " + str(ot))
    return render_template(''+strin+'.html', DATA=ot)



# @app.route('/quests')
# def quests():
#     return render_template('quests.html')


# @app.route('/library')
# def library():
#     return render_template('library.html')


# @app.route('/videos')
# def videos():
#     return render_template('videos.html')


# @app.route('/events')
# def events():
#     return render_template('events.html')


# @app.route('/events/<int:event_id>')
# def event_detail(event_id):
#     return render_template('event_detail.html', event_id=event_id)


# @app.route('/quests/<int:quest_id>')
# def quest_detail(quest_id):
#     return render_template('quest_detail.html', quest_id=quest_id)


# @app.route('/videos/<int:video_id>')
# def video_detail(video_id):
#     return render_template('video_detail.html', video_id=video_id)


if __name__ == '__main__':
    app.run(debug=True)
