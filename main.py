from flask import Flask, render_template
app = Flask(__name__)


PLAYER_DIRECTIONS = {
    1: 'forward',
    2: 'backward'
}


@app.route('/')
def hello():
    return render_template('main.html')


@app.route('/<int:player>/<direction>/')
def change_direction(player, direction):
    if player not in [1, 2] or direction not in ['forward', 'backward']:
        return 'invalid input: {} {}'.format(player, direction)

    PLAYER_DIRECTIONS[player] = direction
    return 'successful'


@app.route('/stats/')
def get_stats():
    return PLAYER_DIRECTIONS[1].upper()


@app.route('/dashboard/')
def get_dashboard():
    return render_template('stats.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
