# antlr-spthy
An ANTLR grammar for spthy files. 

This repo contains an ANTLR grammar for [Tamarin's](https://tamarin-prover.github.io/) spthy format. Tamarin uses a custom spthy parser internally, so this grammar is reverse engineered from the source. 

To develop with it, you will need the complete ANTLR4 tool and runtime, which can be found [here](https://www.antlr.org/download/antlr-4.7.2-complete.jar). In order to use the `test.sh` debug script, you will also need to ensure the ANTLR4 Jar is on your java classpath. 

This project is currently a work in progress and cannot yet parse spthy files correctly. 
