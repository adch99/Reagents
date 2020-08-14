# Reagents PDF in LaTeX

## Overview

1. Each reagent gets a section to itself.
2. Each section has a header image followed by text.
3. All the content is read from a CSV/Excel file.
4. The spreadsheet has the following columns:
  a. Reagent Name (in LaTeX notation)
  b. Plain ASCII Name (for making hyperlinks, not visible to reader)
  c. Image Filename for Header Image
  d. Image Name for Header Image
  e. Filename for Text and other content following the header.
  
## Operating Procedure

1. The user adds entries to the CSV file for each reagent.
2. Each of those entries links to an image file (optional) and
  a text file.
3. The text file is in the ".tex" format and resides in the `txt`
  folder. The ".tex" extension is optional, but it is ultimately
  read as part of a LaTeX file, so this is recommended.
4. The image files all reside in the `img` folder. Most image formats
  like png, jpeg will work.
5. The user then runs the python script `creator.py` which generates
  the `output.tex` file.
6. The `output.tex` file is then compiled using `pdflatex` to produce
  `output.pdf`.
  
## Instructions for Use

1. First off, download this repository from GitHub. Click on the green 'Code'
  button and download as zip. Extract the zip file in a convenient folder.
2. Take all the images that you want to add to the document. Name them properly
  so that they are easily identifiable by the filename. Copy all of them to the
  `img` folder.
3. For each reagent create a `tex` file that contains the text you want to put
  for this reagent. This can contain explanatory text, equations, links, even
  adding more images is possible. Save this file with an appropriate name in the
  `txt` folder.
4. Use Excel and edit the CSV file. Remove the dummy entries that have been put
  there and start adding each of your reagents one by one.
  
## Setup Instructions

To be addded.

## Instructions for Making the `tex` Files

To be added.