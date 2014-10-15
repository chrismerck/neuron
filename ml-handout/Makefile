# moved over to TeX

base=ml-handout

all: $(base).pdf
	open $(base).pdf
	#open $(fig_pngs)

#%.png: %.gv
#	dot -Tpng $< > $@

#%.png: %.fig.pdf
#	convert -density 100 $< $@

%.pdf: %.tex 
	pdflatex $<

clean:
	rm -f *.docx *.pdf *.log *.aux

