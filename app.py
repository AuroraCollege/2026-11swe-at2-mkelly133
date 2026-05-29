from flask import Flask, render_template, request
from wumpus import HuntTheWumpus
from minesweeper import MinesweeperGame

wumpus_game = HuntTheWumpus()
ms = MinesweeperGame()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wumpus', methods=['POST', 'GET'])
def wumpus():
    if request.method == 'POST':
        message = wumpus_game.play(request.form)
    else:
        message = wumpus_game.new_game()
    return render_template('wumpus.html', message=message, game=wumpus_game)

@app.route('/minesweeper')
def minesweeper():
    if request.args.get('new'):
        ms.newGame()
    id = request.args.get('id')
    if id:
        ms.click(id)
    return render_template('minesweeper.html', game=ms)

if __name__ == "__main__":
    app.run()