export PYTHONPATH = .

YEAR?=2019

CUR_SLNS=$(shell ls ${YEAR}/day* | cut -d / -f2 |sort -n)

all: ${CUR_SLNS}

%:
	python ${YEAR}/$@

.PHONY: all
