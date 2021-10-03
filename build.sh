#!/bin/bash

cd pages

#docs
make clean
make html
cp -r _build/html/* ../docs/