H1

# github-json_to_xml

H2

Converter formato de dados na API do GitHub (json para xml)

H2

Usage

$ git remote -v
origin  https://github.com/aeonaxan/demo (fetch)
origin  https://github.com/aeonaxan/demo (push)

$ git convert origin ssh
Successfully changed origin URL to [git@github.com:aeonaxan/demo.git]

$ git remote -v
origin  git@github.com:aeonaxan/demo.git (fetch)
origin  git@github.com:aeonaxan/demo.git (push)

$ git convert origin https
Successfully changed origin URL to [https://github.com/aeonaxan/demo]
Note: Here convert is aliased to github-url-converter

H2

Installation

H6
You can easily install with pip

pip install github-url-converter
Now you can use a git alias for github-url-converter so you dont have to type the whole thing again. Github-url-converter will happily alias itself to convert for you

$ github-url-converter install
github-url-converter aliased to git convert
Now you can use use it as git convert in any git repository.

H2

Licence

MIT