from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/result", methods=["POST"])
def get_result():
    data = request.json
    user_choice = data["user_choice"]
    computer_choice = data["computer_choice"]
    result = determine_winner(user_choice, computer_choice)
    return jsonify({"result": result})

def determine_winner(user, computer):
    if user == computer:
        return "It's a draw!"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"

if __name__ == "__main__":
    app.run(debug=True)
v 