#!/bin/bash
convert -background white -density 132x132 "$1" "${1%%.svg}.png"
