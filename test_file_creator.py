# Test File Creator

text = """
Some text for reagent number {0}.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent accumsan tincidunt lorem nec lobortis. Phasellus finibus tellus sagittis tincidunt placerat. Nam sem arcu, sollicitudin ac accumsan vitae, convallis id mi. Etiam non enim ante. Integer pulvinar luctus urna. In vel sem et quam ultrices efficitur. Donec a arcu nunc. Vestibulum quis ultrices enim. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;

Cras a ante est. Sed sed laoreet mi. Phasellus ornare ornare nisl, ac laoreet urna sagittis in. Duis vel est mauris. Suspendisse laoreet massa nibh, nec pretium lorem tincidunt nec. Aliquam erat volutpat. Mauris pretium dapibus urna, nec varius dolor mollis et.
"""

for i in range(1, 13):
	ofile = open(f"txt/reagent{i}.tex", "w")
	ofile.write(text.format(i))
	ofile.close()