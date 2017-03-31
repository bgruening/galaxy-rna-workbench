
all: README.md.new

README.md.new:
	python scripts/generate_readme.py


clean:
	rm -f README.md.new
