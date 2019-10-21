# antlr-spthy

[![CircleCI](https://circleci.com/gh/galadran/antlr-spthy.svg?style=svg)](https://circleci.com/gh/galadran/antlr-spthy)

An ANTLR grammar for spthy files. 

This repo contains an ANTLR grammar for [Tamarin's](https://tamarin-prover.github.io/) spthy format. Tamarin uses a custom spthy parser internally, so this grammar is reverse engineered from the source. 

To develop with it, you will need the complete ANTLR4 tool and runtime, which can be found [here](https://www.antlr.org/download/antlr-4.7.2-complete.jar). Just wget it into your repo and run test.sh

This project is currently a work in progress and cannot yet parse spthy files correctly. *CircleCI will build any PRs and shows the latest test results to any logged in user*

# Documentation 

This repo consists of a number of distinct working parts. Firstly, use either the master branch for the nearly-prime model or the prime branch for the prime model. The differences are very slight and will be integrated into a command line switch in due course. 

A lot of work remains to be done to clean up the code and leave it in a maintainable state.

## allTogether.py

Contains the wrapper function which given the contents of a spthy as a UTF-8 string, will produce a transformed UTF-8 string with the new DH model. This is the highest level wrapper which handles an entire spthy

## convert.py

Given a particular token stream, perform the syntactical manipulation on a set of rules. This sits between the overall spthy transformation and the underlying parsing of the relevant rules. 

## convertWhole.py

Parses a spthy into "rules" and everything else, ignoring comments. 

## gen_py.sh

When Tamarinrule.g4 is updated, run this bash script to regenerate the python classes and copy them into the subdirectories for each part of the transformation. 

## letSubstitution (DIR)

This directory handles the transformation of a rule with let bindings into a generic rule without any let bindings. 

## makeDH (DIR)

This directory handles the transformation of a rule without let bindings and a traditional DH model into the 'base case' of new DH model. Specifically, it maps DH elements into either new constant elements or new variable elements, depending on whether they are constructed from constants/fresh values or variables. It does not parse out any non-constant exponents, create any actions or so on. 

## refineDH

This directory handles the transformation of rule in the 'base case' into a finsihed rule. It does this by visiting each rule in order and transforming out all the exponentiations. This includes adding the appropriate raised facts and intermediate representations. 

## Tamarin.g4.original

This file contains the original ANTLR4 grammar for Tamarin as provided to me. It does not work.

## Tamarin.g4

This file contains a modified version of the Tamarin ANTLr4 grammar. It does not work, in particular because ANTLR's eager lexer gets confused. It needs to be split into a lexer and a parser sub grammars. Then the lexer grammar needs enhancing with distinct modes to avoid over eager parsing by restricting what keywords we expect. 

## Tamarinrule.g4

This is an ANTLR4 grammar I created which can handle rules, but not other aspects of Tamarin's grammar (e.g. lemmas, axioms and so on). 

## test_rule.sh

This bash script generates and tests a Tamarin Rule grammar using ANTLR's Java debugger. 

## test.sh

This bash script generates and tests a Tamarin grammar using ANTLR's Java debugger.