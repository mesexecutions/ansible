#!/bin/bash

files=()
search_string1="password"
search_string2="pam_unix.so"

files+=($(find / -type f \( -name "password-auth" -o -name "system-auth" \)))

for file in "${files[@]}"; do
    value=$(grep -E "($search_string1.*$search_string2|$serach_string2.*$search_string1)" "$file")
    echo $(hostname) $value "####" $file
done
