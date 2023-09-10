docker stop mkdocs-miniprintbox
docker run --name mkdocs-miniprintbox --rm -it -v ${PWD}:/docs squidfunk/mkdocs-material build
