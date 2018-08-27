from flask import Flask, render_template, request
import re


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


@app.route('/dto_java', methods=['POST'])
def dto_gen_java():
	area = request.form['area']
	return generate_dto_java(area)


def lower_one(s):
	return s[0].lower() + s[1:] if len(s) > 0 else s


def generate_dto_java(area):
	result = ''
	dto_tags = []

	for line in area.split('\n'):
		if line.strip():
			dto_tags.append(re.split(r'[><]', line.strip())[1].upper())

	for i, tag in enumerate(dto_tags):
		if i == len(dto_tags) - 1:
			result += '\tprivate String {:s};'.format(tag)
		else:
			result += '\tprivate String {:s};\n'.format(tag)

	for tag in dto_tags:
		result += '\n\n\tpublic String get{:s}() {}\n\t\treturn Utilidades.trim({:s});\n\t{}'.format(tag, unichr(123), tag, unichr(125))

	for tag in dto_tags:
		result += '\n\n\tpublic set{:s}(String {:s}) {}\n\t\tthis.{:s} =  {:s};\n\t{}'.format(tag, lower_one(tag), unichr(123), tag, tag, unichr(125))

	return result



if __name__ == '__main__':
	app.run(debug=True)