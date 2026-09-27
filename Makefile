# Book production. `make` on its own builds everything for the default book;
# pass BOOK=<slug> for another one. The series:
#
#   1  depois-de-mim   2  o-elevador   3  recife-submersa
#
#   make BOOK=o-elevador all        epub + interior pdf + cover
#   make books                      all three books, one after another
#   make epub / print / cover       one target at a time
#   make check                      KDP preflight + both manuscript gates
#   make fios                       setups without payoffs, payoffs without setups
#   make marcadores                 unresolved [[?...]] markers
#   make watch                      rebuild the print pdf as you write
#   make stats                      word counts, pacing, POV balance
#   make digest                     whole-novel map, for reviewing a chapter
#   make outline                    docs/$(BOOK)/outline.md -> chapter files
#   make chapter TITLE="..."        add a chapter outside the outline
#   make clean

BOOK  ?= depois-de-mim
BOOKS := $(notdir $(wildcard books/*))
PY   := python3
DIST := dist/$(BOOK)

.DEFAULT_GOAL := all
.PHONY: all books epub print cover check fios marcadores watch stats digest outline \
        clean new-book chapter open deps release

all:
	@$(PY) scripts/build.py $(BOOK) --all

books:
	@for b in $(BOOKS); do $(PY) scripts/build.py $$b --all || exit 1; done

epub:
	@$(PY) scripts/build.py $(BOOK) --epub

print:
	@$(PY) scripts/build.py $(BOOK) --print

cover:
	@$(PY) scripts/build.py $(BOOK) --cover

check: marcadores fios
	@$(PY) scripts/check.py $(BOOK)

# The novel's structural gate: a promise the book makes and never keeps, or a
# payoff the book never set up. Both are invisible in one chapter.
fios:
	@$(PY) scripts/check-threads.py $(BOOK)

# Invented rules, unchecked facts and open authorial decisions still marked in
# the manuscript. A chapter cannot be `revised` or `final` while one stands.
marcadores:
	@$(PY) scripts/check-claims.py $(BOOK)

release: all check
	@echo "\nReady to upload from $(DIST)/:"
	@ls -lh $(DIST)/*.epub $(DIST)/*.pdf 2>/dev/null | awk '{print "  " $$9 "  " $$5}'

stats:
	@$(PY) scripts/stats.py $(BOOK)

# POV, story time, threads, seeds and payoffs for every chapter, plus the
# reports. Read this before reviewing a chapter against the novel.
digest:
	@$(PY) scripts/digest.py $(BOOK)

# docs/$(BOOK)/outline.md is the single source for chapter titles and numbering.
# Never touches a body you have written.
outline:
	@$(PY) scripts/scaffold-outline.py $(BOOK)

# Rebuilds on every save. Needs `brew install fswatch`.
watch:
	@command -v fswatch >/dev/null || { echo "brew install fswatch"; exit 1; }
	@$(PY) scripts/build.py $(BOOK) --print
	@fswatch -o books/$(BOOK) shared | while read _; do \
		$(PY) scripts/build.py $(BOOK) --print; done

open:
	@open $(DIST)/$(BOOK)-interior.pdf

new-book:
	@test -n "$(SLUG)" || { echo "usage: make new-book SLUG=<slug> [TITLE=\"...\"]"; exit 1; }
	@$(PY) scripts/new-book.py "$(SLUG)" $(if $(TITLE),--title "$(TITLE)",)

chapter:
	@test -n "$(TITLE)" || { echo "usage: make chapter TITLE=\"...\" [BOOK=$(BOOK)]"; exit 1; }
	@$(PY) scripts/new-chapter.py $(BOOK) "$(TITLE)"

# Everything the toolchain needs, on macOS.
deps:
	brew install pandoc typst imagemagick qpdf poppler epubcheck fswatch

clean:
	rm -rf dist
