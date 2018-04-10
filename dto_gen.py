from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def hello_world():
	return render_template('index.html')


@app.route('/dto_gen', methods=['POST'])
def dto_gen():
	indent = request.form['indent']
	tag = request.form['tag']
	pic = request.form['pic']
	name = request.form['name']
	return generate_dto(indent, tag, pic, name)


def generate_dto(indent, tag, pic, name):
	dto = ('{} FILLER' + ' '*14 + 'PIC X({:02d}) VALUE \'<{}>\'.\n').format(indent, len(tag)+2, tag.upper())
	dto += ('{} WX-DTO{}' + ' '*(14-len(name)) + 'PIC X({:02d}) VALUE SPACES.\n').format(indent, name.upper(), int(pic))
	dto += ('{} FILLER' + ' '*14 + 'PIC X({:02d}) VALUE \'</{}>\'.\n').format(indent, len(tag)+3, tag.upper())
	return dto


if __name__ == '__main__':
	app.run(debug=True)