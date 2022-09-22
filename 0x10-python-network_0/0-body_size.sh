#!/bin/bash
# displays the size of the body of an http response in bytes
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
