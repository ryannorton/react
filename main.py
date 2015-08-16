import json

from flask import Flask, render_template


app = Flask(__name__)


PLAYER_DIRECTIONS = {
    1: 'forward',
    2: 'backward'
}

INTENSITY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


@app.route('/')
def hello():
    return render_template('main.html')


@app.route('/<int:player>/<direction>/')
def change_direction(player, direction):
    if player not in [1, 2] or direction not in ['forward', 'backward']:
        return 'invalid input: {} {}'.format(player, direction)

    PLAYER_DIRECTIONS[player] = direction
    return 'successful'


@app.route('/intensity/<int:intensity>/')
def set_intensity(intensity):
    global INTENSITY
    INTENSITY.append(intensity)
    INTENSITY = INTENSITY[1:]
    print INTENSITY
    return 'success'


@app.route('/stats/')
def get_stats():
    return json.dumps({
        'direction': PLAYER_DIRECTIONS[1].upper(),
        'intensity': str(min(sum(INTENSITY) / len(INTENSITY) / 3, 100))
    })


@app.route('/dashboard/')
def get_dashboard():
    return render_template('stats.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
