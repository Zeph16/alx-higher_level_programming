#!/bin/bash
# sends a header called X-HolbertonSchool-User-Id with the value 98
curl -s "$1" -H "X-School-User-Id: 98"
