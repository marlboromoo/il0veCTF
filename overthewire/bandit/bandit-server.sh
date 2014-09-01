#!/bin/bash

if [[ -z "$1" ]]; then
    exit 0
else
    ssh bandit"$1"@bandit.labs.overthewire.org
fi

