# EnkaCard-web
A static web page generator for EnkaCard

This project is to provide a static page generator that could be deployed to
your personal website based on [EnkaCard](https://github.com/DEViantUA/EnkaCard)
project.

Since the profile is generated in image form, the web
page generated is not as interactive as the original https://enka.network/,
but it is enough for most use cases.

## Usage

Install the dependencies:
```bash
pip install -r requirements.txt
```

And run the script, pass the uid as the argument:
```bash
python main.py -u 273518546
```
If you want to change the language, for example, to Chinese (Simplified), then use:
```bash
python main.py -u 273518546 -l chs
```
You could get more help by
```bash
python main.py -h
```

After the generation, you could open `enkacard.html` directly to preview the result. You could directly deploy those files to your website.
