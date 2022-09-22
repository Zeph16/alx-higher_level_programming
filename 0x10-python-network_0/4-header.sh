#!/bin/bash
# sends a header called X-HolbertonSchool-User-Id with the value 98
curl -s -H "X-School-User-Id: 98" "$1"
