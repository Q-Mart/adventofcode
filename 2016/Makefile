# Makefile kindly provided by github.com/LordAro
CC=gcc
FLAGS=-g -Wall -Wextra -pedantic -std=c++1y

CUR_SLNS=$(shell ls src/day* | cut -d/ -f2 | cut -d. -f1 | cut -dy -f2 | sort -n)

all: ${CUR_SLNS}

%:
	@echo -e '\x1b[1;34mCompiling day $@ solution\x1b[0m'
	${CXX} -o builds/day$@ ${FLAGS} ${FLAGS_DAY_$@} src/day$@.cpp
	@./builds/day$@

.PHONY: all
