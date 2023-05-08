from flask import Flask, render_template, request
import subprocess

app = Flask(__name__,template_folder='webpages')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/firewall', methods=['POST'])
def firewall():
    command = request.form['command']
    output = subprocess.check_output(command.split())
    output_str = output.decode('utf-8')
    output_lines = output_str.split('\n')
    output_str_newline = '\n'.join(output_lines)

    command1 = request.form['command1']
    output1 = subprocess.check_output(command1.split())
    output_str1 = output1.decode('utf-8')
    output_lines1 = output_str1.split('\n')
    output_str_newline1 = '\n'.join(output_lines1)
    mainoutput=output_str_newline+"\n**************\n"+output_str_newline1

    return render_template('firewall.html', output=mainoutput)

if __name__ == '__main__':
    app.run(debug=True)
