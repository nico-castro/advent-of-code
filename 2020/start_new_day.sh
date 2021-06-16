#!/bin/bash

usage() {
  echo """
NAME
  start_new_day

SYNOPSIS
  ./start_new_day.sh [day]

DESCRIPTION
  This script will create a new directory named after the provided day and will put a Hello World
  python script into it - q1_answer.py. Additionally, it will create a README file that contains
  a description of the question pulled from the AoC site.

  Example:
    Command line:
    $ ./start_new_day.sh 1

    Directory Tree:
    1/
    ├──  q1_answer.py
    └──  README.md

    File Contents:
    ------------
    1 #!/usr/local/bin/python3
    2
    3 def main():
    4     print("Hello world!")
    5
    6 if __name__ == "__main__":
    7     main()
    8

"""
}

help() {
  usage && exit 1
}

die() {
  local red="\\033[38;5;196m"
  local no_color="\\033[0m"
  echo -e $red$1$no_color && exit 1
}

main() {
  if [[ ! $# -eq 1 ]]; then
    help
  fi
  local day=$1

  if [[ -e "$day" ]]; then
    die "You've already started this day!"
  fi

  mkdir $day && cd $day
  echo """#!/usr/local/bin/python3

def main():
    print(\"Hello World!\")

if __name__ == \"___main__\":
    main()
""" >q1_answer.py

  chmod +x q1_answer.py
  curl -L "https://adventofcode.com/2020/day/$1" >README.html

}

main $@  
