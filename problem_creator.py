

problem_template = """<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>brainfuck</title>
</head>

<style type="text/css">

textarea {
	display: block;
}

input, select, textarea {
color: #e67b5e;
}

.container {
	display: flex;
	flex-direction: column;
}

.center {
	margin: auto;
	width: 50%;
}

.button {
	width: 80px;
	background-color: black;
	color: white;
}

.text {
	text-align: center;
}

.outputt {
	color: white;
	word-break: break-all;
    white-space: normal;
}

.intsbox {
	color: white;
}

.stringsout {
	color: white;
}

.inputbuttons {
	display: flex;
}

</style>

<script type="text/javascript" src="logic.js"> </script>

<script type="text/javascript">
	function startprogram() {

		var answ = SOLUTION;

		defineProblem(answ, OUTPUT_TYPE, INPUT_TYPE, "PROBLEM_NAME", CHARS_LIMIT);
		attempt();	
	}
</script>
<body background="bg_dark.jpg">
	
	<div class="center">
		<div class="text">
			<h1><a href="index.html" style="color:#666666">PROBLEM_NAME</a></h1>
			<p style="color:#666666;">DESCRIPTION</p>
		<div>

		  <div class="container">
		  		<textarea id="bfinput" name="brainfuck_input" rows="20" cols="90" style="background-color:#0d1018;"></textarea>

		  		<!---  see logic.js for the parameters. string, type, take char or num-->
		   		<br><br>
		   		<div class="inputbuttons">
		   			<button type="button" class="button" onclick="startprogram()">Run</button>
		   			<input type="checkbox" id="chkbox">
		   			<label style="color:#666666">append newline character to single character input?</label>
		   		</div>
		   		<br><br>
		   		<textarea id="intsout" class="intsbox" name="integersout" rows="5" cols="90" style="background-color:#000000;"></textarea> 	
		  		<textarea id="outstr" class="stringsout" name="stringsoutput" rows="5" cols="90" style="background-color:#000000;"></textarea> 	

		</div>
	</div>
</body>
</html>
"""

solution = ""
i = 1
while i <= 255:
	solution += str(i) + ' '
	i += 2

solution = solution[:-1]

# 0 string, 1 numbers
output_type = 1

# 0 chars, 1 number
input_type = 0

# name
problem_name = "Odd Numbers"

# problem description
problem_description = "Your task is to output odd numbers from 1 to 255 in the first textarea (numeric output will be judged)"

# character limit
chars_limit = 11

problem_template = problem_template.replace("SOLUTION", '"' + solution + '"')
problem_template = problem_template.replace("OUTPUT_TYPE", str(output_type))
problem_template = problem_template.replace("INPUT_TYPE", str(input_type))
problem_template = problem_template.replace("PROBLEM_NAME", problem_name)
problem_template = problem_template.replace("DESCRIPTION", problem_description)
problem_template = problem_template.replace("CHARS_LIMIT", str(chars_limit))

def replace_spaces(string):
	newstr = ""
	for ch in string:
		if ch == ' ':
			newstr += '_'
		else:
			newstr += ch

	return newstr

problemfile = open(replace_spaces(problem_name) + '.html', 'w')
problemfile.write(problem_template)
problemfile.close()
