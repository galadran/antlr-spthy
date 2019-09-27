# antlr-spthy

[![CircleCI](https://circleci.com/gh/galadran/antlr-spthy.svg?style=svg)](https://circleci.com/gh/galadran/antlr-spthy)

An ANTLR grammar for spthy files. 

This repo contains an ANTLR grammar for [Tamarin's](https://tamarin-prover.github.io/) spthy format. Tamarin uses a custom spthy parser internally, so this grammar is reverse engineered from the source. 

To develop with it, you will need the complete ANTLR4 tool and runtime, which can be found [here](https://www.antlr.org/download/antlr-4.7.2-complete.jar). Just wget it into your repo and run test.sh

This project is currently a work in progress and cannot yet parse spthy files correctly. *CircleCI will build any PRs and shows the latest test results to any logged in user*
