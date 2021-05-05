import bottle
import model

vislice = model.Vislice() #model.(to napisemo ker mormo povedat iz kerga razdelka uvazamo class) class Vislice

@bottle.get('/')
def index():
    return bottle.template('index.tpl')
    # funk opremimo z dekoratorjem @bottle.get(naslov url)...('/')...pomeni korenska stran

bottle.run(reloader=True, debug=True)