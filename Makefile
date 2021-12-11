export PYTHONPATH = .

YEAR?=2021

CUR_SLNS=$(shell python sorted_days.py ${YEAR})

all: ${CUR_SLNS}

%:
	python3 ${YEAR}/$@

.PHONY: all
