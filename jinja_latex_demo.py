import jinja2
import os
from jinja2 import Template
latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)
template = latex_jinja_env.get_template('reagent_template.tex')
text = r"""
Hello world! Let's see if \chem{Au_4_O^9} and Cu_2 Cl_2 render properly.

Along with all this stuff like.
\begin{itemize}
\item What

\item A

\item Wonderful
\item World!
\end{itemize}
"""
print(template.render(sectionName="Hello", imagefilename="hello.png", imagename="helloimage", text=text))