from enkacard import encbanner
from enkacard.src.utils.pill import get_dowload_img
from enkacard.src.utils.translation import supportLang
import argparse
import traceback

import asyncio
import os, shutil

parser = argparse.ArgumentParser(prog='ENKA Card Web',
            description='A static web page generator for EnkaCard')
parser.add_argument('--uid', '-u', metavar='U', type=str, help="account uid", required=True)
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

uid       = args.uid
outputdir = args.outputdir
imgdir    = outputdir if args.imgdir is None else args.imgdir
lang      = args.lang
preserve  = args.preserve

if os.path.exists(outputdir):
    if not preserve:
        shutil.rmtree(outputdir)
os.makedirs(outputdir, exist_ok=True)

async def generate_cards():
    async with encbanner.ENC(lang=lang, uid=uid) as encard:
        # get info
        profile_result = await encard.profile(card=True)
        print(profile_result)
        profile_result.card.convert('RGB').save(os.path.join(outputdir, 'profile.jpg'))

        character_wide_result = await encard.creat(template=2)
        print(character_wide_result)
        character_narrow_result = await encard.creat(template=1)
        print(character_narrow_result)
        
        character_list_str = []
        for character in encard.enc.characters:
            character_name = character.name.replace(' ','_')
            # avatar
            character_avatar = await get_dowload_img(character.image.icon.url)
            character_rarity = character.rarity
            character_fullname = "{}-{}".format(character_name, character_rarity)
            character_avatar.save(
                os.path.join(outputdir, 'avatar-{}.png'.format(character_fullname)))
            character_list_str.append('"' + character_fullname + '"')

        for card in character_wide_result.card:
            character_name = card.name.replace(' ','_')
            character_rarity = card.rarity
            character_fullname = "{}-{}".format(character_name, character_rarity)
            card.card.save(os.path.join(outputdir, 'wide-{}.png'.format(character_fullname))) # FIXME: black background when use jpg
        
        for card in character_narrow_result.card:
            character_name = card.name.replace(' ','_')
            character_rarity = card.rarity
            character_fullname = "{}-{}".format(character_name, character_rarity)
            card.card.convert('RGB').save(
                os.path.join(outputdir, 'narrow-{}.jpg'.format(character_fullname)))
        
        # in case there are more characters in the folder
        for filename in os.listdir(outputdir):
            if 'avatar-' in filename:
                f_character_name = filename.rsplit('.')[0].split('-')[1]
                f_character_rarity = filename.rsplit('.')[0].split('-')[2]
                f_character_fullname = '"' + "{}-{}".format(f_character_name, f_character_rarity) + '"'
                if f_character_fullname not in character_list_str:
                    character_list_str.append(f_character_fullname)
        
        # config
        with open("enkacard_config.js", "w") as config_js:
            config_js.write("characters = [{}];\nimgdir = \"{}\"\n".format(
                ', '.join(character_list_str), imgdir))
        
        # finish
        print("\nGeneration finished in dir: {}".format(outputdir))
        print("Config is generated in: enkacard_config.js, image diretory is: {}".format(imgdir))
        print("Web page could be viewed in: enkacard.html")

asyncio.run(generate_cards())
