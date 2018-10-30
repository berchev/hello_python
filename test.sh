#!/usr/bin/env bash

out=$(./hello.py)

echo $out

# we are checking whether "out" variable is the same as "hello"

if [ "${out}" == "hello" ];then
  echo "GOOD: test pass"
else
  echo "BAD: test fail"
  exit 1
fi
