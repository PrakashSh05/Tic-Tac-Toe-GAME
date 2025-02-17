from flask import Flask, render_template, jsonify

app = Flask(__name__)

board = [["" for _ in range(3)] for _ in range(3)]
turn = "X"
winner = None

def check_winner():
    global winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            winner = row[0]
            return winner

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            winner = board[0][col]
            return winner

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        winner = board[0][0]
        return winner

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        winner = board[0][2]
        return winner

    return None

@app.route("/")
def index():
    return render_template("index.html", board=board, turn=turn, winner=winner)

@app.route("/move/<int:row>/<int:col>", methods=["POST"])
def make_move(row, col):
    global turn, winner
    if board[row][col] == "" and winner is None:
        board[row][col] = turn
        winner = check_winner()
        turn = "O" if turn == "X" else "X"

    return jsonify({"board": board, "winner": winner, "turn": turn})

@app.route("/reset", methods=["POST"])
def reset_game():
    global board, turn, winner
    board = [["" for _ in range(3)] for _ in range(3)]
    turn = "X"
    winner = None
    return jsonify({"board": board, "turn": turn})

if __name__ == "__main__":
    app.run(debug=True)
