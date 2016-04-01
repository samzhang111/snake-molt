#!/usr/bin/env bash

sfood -q $1 | sfood-graph | grep '^".*->' | python parse_graph.py

