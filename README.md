# python3-template
python3-template

## Commands to get started

1. Clone this `.git` repository to local machine: 
```bash
git clone https://github.com/wes-o/python3-template.git <template-name> && cd $_
```

2. Checkout a branch currently in development.
```bash
git checkout --track origin/dev
```

3. A good practice is to create, and activate a virtual environment:
```bash
python3 -m venv venv
```
```bash
source venv/Scripts/activate
```

4. Change into directory location of 'python3_template'. Then, run:
```bash
pip install --trusted-host pypi.org setuptools==40.8.0
```

> Specific version chosen based on documented version. See following link for more info.
[https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/#fallback-behaviour]

5. After package installation, try to install local module.
```bash
# first installation
pip install . 
# upgrade existing installation, for version update 
pip install --upgrade .
```

*Test it out locally. 🎵 :musical_note: *
```bash
python3 test.py
```

