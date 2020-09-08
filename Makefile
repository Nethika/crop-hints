
SHELL := /bin/bash

CREDENTIALS := GOOGLE_APPLICATION_CREDENTIALS=~/.googlecloud/mvtango-d5ff4947b961.json 

IMAGES := $(shell ls -1 images/*jpg)
RATIOS := [1,1.779,0.5625]


all: $(IMAGES)

$(IMAGES) :
	$(CREDENTIALS) python crophints.py $@ --ratios='$(RATIOS)'

set:
	echo set -gx $(CREDENTIALS)
