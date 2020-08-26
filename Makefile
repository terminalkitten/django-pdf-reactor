.PHONY: generate-docs

generate-docs:
	pdoc --overwrite --html-dir docs/ --html pdf_reactor
