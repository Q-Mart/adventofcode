export PYTHONPATH = .

YEAR?=2020

CUR_SLNS=$(shell ls ${YEAR}/day* | cut -d / -f2 |sort -n)

all: ${CUR_SLNS}

%:
	python3 ${YEAR}/$@

.PHONY: all
