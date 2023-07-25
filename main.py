from enkacard import encbanner
from enkacard.src.utils.FunctionsPill import imgD
from enkacard.src.utils.translation import supportLang
import argparse

import asyncio
import os, shutil

parser = argparse.ArgumentParser(prog='ENKA Card Web',
            description='A static web page generator for EnkaCard')
parser.add_argument('--uid', '-u', metavar='U', type=str, help="account uid")
parser.add_argument('--outputdir', '-o', metavar='O', type=str, default='genshin',
                    help="image directory for saving (default: genshin)")
parser.add_argument('--imgdir', '-fo', metavar='FO', type=str, default=None,
                    help="final imgdir variable in enkacard_config.js (default: <outputdir>)")
parser.add_argument('--lang', '-l', metavar='L', choices=supportLang.keys(), default='en',
                    help="display language (default: en)")
parser.add_argument('--preserve', '-p', metavar='P', type=bool, default=False,
                    help="whether to preserve previous character runs, " + 
                    "which is useful if you want to display more characters (default: False)")
args = parser.parse_args()

uid            = args.uid
outputdir      = args.outputdir
imgdir         = outputdir if args.imgdir is None else args.imgdir
lang           = args.lang
preserve       = args.preserve

if os.path.exists(outputdir):
    if not preserve:
        shutil.rmtree(outputdir)
os.makedirs(outputdir, exist_ok=True)

async def generate_cards():
    async with encbanner.ENC(lang=lang) as encard:
        # get info
        ENCpy = await encard.enc(uids=uid)

        # profile
        profile_result = await encard.profile(ENCpy, 1)
        print(profile_result)
        profile_result['img'].save(os.path.join(outputdir, 'profile.png'))

        # avatar
        for character in profile_result['characters'].keys():
            character_icon_img = await imgD(profile_result['characters'][character]['image'])
            character_icon_img.save(
                os.path.join(outputdir, 'icon_{}.png'.format(character)))
        
        # character detail
        character_wide_result = await encard.creat(ENCpy, 3)
        print(character_wide_result)
        character_narrow_result = await encard.creat(ENCpy, 7)
        print(character_narrow_result)
        for character in character_wide_result[uid].keys():
            character_wide_result[uid][character]['img'].save(
                os.path.join(outputdir, 'wide_{}.png'.format(character)))
            character_narrow_result[uid][character]['img'].save(
                os.path.join(outputdir, 'narrow_{}.png'.format(character)))
        
        # config
        character_list_str = []
        for filename in os.listdir(outputdir):
            if 'wide_' in filename:
                character_list_str.append('"' + filename.split('_')[1].rsplit('.')[0] + '"')
        with open("enkacard_config.js", "w") as config_js:
            config_js.write("characters = [{}];\nimgdir = \"{}\"\n".format(
                ', '.join(character_list_str), imgdir))
        
        # finish
        print("\nGeneration finished in dir: {}".format(outputdir))
        print("Config is generated in: enkacard_config.js, image diretory is: {}".format(imgdir))
        print("Web page could be viewed in: enkacard.html")

asyncio.run(generate_cards())
