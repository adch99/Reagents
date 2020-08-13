import pandas as pd
import jinja2
import os

outfilename = "output.tex"
datafilename = "data.csv"

templatefilename = "document_template.tex"
section_template_filename = "reagent_template.tex"
working_indicator = "% Working Area\n"

def createSections(outfile):
    print("Working Function")
    sections = getSections()
    for section in sections:
        sectionText = createSection(section)
        outfile.write(sectionText)
        outfile.write("\n")

def createSection(sectionDict):
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
    # This excellent notation has been taken from Brad Erickson's blog
    # See this for more details: https://bit.ly/3gTaH3z
    template = latex_jinja_env.get_template('reagent_template.tex')

    textFilename = sectionDict["textFilename"]
    if textFilename != "":
        with open("txt/"+textFilename, "r") as textFile:
            text = textFile.read()
    else:
        text = ""

    output = template.render(**sectionDict)
    output += "\n"
    output += text
    
    return output

def getSections():
    data = pd.read_csv(datafilename, encoding="utf-8", header=0, delimiter=",")
    return data.to_dict("records")

# End of Functions

outfile = open(outfilename, "w")
# First we copy the beginning of the document from the template
templatefile = open(templatefilename, "r")
buffer = templatefile.readlines()
templatefile.close()

for line in buffer:
    if line != working_indicator:
        outfile.write(line)
    else:
        createSections(outfile)

outfile.close()