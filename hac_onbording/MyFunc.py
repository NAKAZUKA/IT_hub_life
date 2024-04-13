import os.path
from werkzeug.utils import secure_filename
import BD

def Events():
    events = BD.get_question("SELECT id, name, date FROM EVENTS")
    print(events)
    return events


def Event_detail(id):
    event = BD.get_question("SELECT * FROM EVENTS WHERE id==" + str(id))
    # organizator = event[0]['id_club']
    event[0]['club'] = BD.get_question("SELECT * FROM CLUBS WHERE id==" + str(event[0]['id_club']))[0]['name']
    event[0]['president'] = BD.get_question("SELECT FIO FROM USERS WHERE id in ( SELECT id_user FROM USER_CLUB WHERE id_club=="+str(event[0]['id_club'])+" ) and role in (SELECT id FROM ROLES WHERE comment == 'президент клуба' )")[0]['FIO']
    # event[0]['organizator'] = dol +' '+ event[0]['organizator'][0]['FIO']
    print("ret "+str(event))

    # event[0]['president'] = '1'
    # event[0]['club'] = '2'
    return event


def Quests():
    events = BD.get_question("SELECT * FROM QUESTS")
    print(events)
    return events


def Quest_detail(id):
    events = BD.get_question("SELECT * FROM QUESTS WHERE id==" + str(id))
    # questions = BD.get_question("SELECT * FROM QUESTS_QUESTION WHERE id_quest==" + str(id))
    # events[0]['questions'] = questions
    events[0]['events'] = BD.get_question("SELECT * FROM EVENTS WHERE id_quest==" + str(id))
    events[0]['organizators'] = BD.get_question("SELECT * FROM CLUBS WHERE id in (SELECT id_club FROM EVENTS WHERE id_quest==" + str(id) + ')')
    print(events)
    return events


def Library(path, file, id):
    def_path = path
    group = str(BD.get_question("SELECT gruppa FROM USERS WHERE id==" + str(id))[0]['gruppa'])
    print(group)
    path = "static/DATA/FILES/" + group + '/' + path
    kr_path = "DATA/FILES/" + group

    if file != '':
        uploads = os.path.join(path)
        return uploads

    from os import listdir
    from os.path import isfile, join
    files = [f for f in listdir(path)]
    paths = []
    file = []
    for i in files:
        if os.path.isdir(path + '/' + i):
            paths.append({'path': i})
        else:
            file.append({'file': i, 'allfile': (kr_path + '/' + i)})
    files = file
    return {'paths': paths, 'files': files, 'mypath' : def_path}


def Clubs():
    events = BD.get_question("SELECT * FROM CLUBS")
    print(events)
    return events


def Club_detail(id):
    events = BD.get_question("SELECT * FROM CLUBS WHERE id==" + str(id))
    events[0]['president'] = BD.get_question("SELECT * FROM USERS WHERE id in ( SELECT id_user FROM USER_CLUB WHERE id_club=="+str(id)+") and role in (SELECT id FROM ROLES WHERE comment=='президент клуба')")[0]
    events[0]['reiting'] = BD.get_question("SELECT * FROM CLUBS ORDER BY reiting DESC")
    for i in range(len(events[0]['reiting'])):
        if str(events[0]['reiting'][i]['id']) == str(id):
            events[0]['reiting'] = id
            break

    events[0]['ychastniki'] = BD.get_question("SELECT FIO FROM USERS WHERE id in ( SELECT id_user FROM USER_CLUB WHERE id_club=="+str(id)+")")
    events[0]['events'] = BD.get_question("SELECT * FROM EVENTS WHERE id_club==" + str(id))
    print(events)
    return events


def Profile(id):
    events = BD.get_question("SELECT * FROM USERS WHERE id=="+str(id))
    events[0]['interests'] = events[0]['interests'].split()
    events[0]['clubs'] = BD.get_question("SELECT * FROM CLUBS WHERE id in (SELECT id_club FROM USER_CLUB WHERE id_user in (SELECT id FROM USERS WHERE id=="+str(id)+"))")
    print(events)
    return events


def Rating():
    events = BD.get_question("SELECT * FROM CLUBS")
    events[0]['raiting'] = BD.get_question("SELECT * FROM CLUBS ORDER BY reiting DESC")
    # for i in range(len(events[0]['reiting'])):
        # if str(events[0]['reiting'][i]['id']) == str(id):
        #     events[0]['reiting'] = id
        #     break

    # events[0]['ychastniki'] = BD.get_question("SELECT FIO FROM USERS WHERE id in ( SELECT id_user FROM USER_CLUB WHERE id_club=="+str(id)+")")
    # events[0]['events'] = BD.get_question("SELECT * FROM EVENTS WHERE id_club==" + str(id))
    print(events)
    return events


def Friends():
    events = BD.get_question("SELECT * FROM USERS")
    for i in range(len(events)):
        # print(events[i]['id'])
        events[i]['clubs'] = BD.get_question("SELECT * FROM CLUBS WHERE id in (SELECT id_club FROM USER_CLUB WHERE id_user=="+str(events[i]['id'])+")")
        ev = []
        for u in events[i]['clubs']:
            ev.append(u['name'])
        ev = ', '.join(ev)
        events[i]['clubs'] = ev
    return events