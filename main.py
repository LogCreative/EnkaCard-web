from enkacard import encbanner
from enkacard.src.utils.FunctionsPill import imgD

import asyncio
import os, shutil

uid = "273518546"
outputdir = "genshin"
lang = "chs"
preserve = False         # preserve previous character runs

if os.path.exists(outputdir):
    if not preserve:
        shutil.rmtree(outputdir)
else:
    os.makedirs(outputdir)

async def generate_cards():
    async with encbanner.ENC(lang=lang) as encard:
        ENCpy = await encard.enc(uids=uid)

        profile_result = await encard.profile(ENCpy, 1)
        print(profile_result)
        profile_result['img'].save(os.path.join(outputdir, 'profile.png'))

        for character in profile_result['characters'].keys():
            character_icon_img = await imgD(profile_result['characters'][character]['image'])
            character_icon_img.save(
                os.path.join(outputdir, 'icon_{}.png'.format(character)))
        
        character_wide_result = await encard.creat(ENCpy, 3)
        print(character_wide_result)
        character_narrow_result = await encard.creat(ENCpy, 7)
        print(character_narrow_result)

        for character in character_wide_result[uid].keys():
            character_wide_result[uid][character]['img'].save(
                os.path.join(outputdir, 'wide_{}.png'.format(character)))
            character_narrow_result[uid][character]['img'].save(
                os.path.join(outputdir, 'narrow_{}.png'.format(character)))
        
        character_list_str = []
        for filename in os.listdir(outputdir):
            if 'wide_' in filename:
                character_list_str.append('"' + filename.split('_')[1].rsplit('.')[0] + '"')
        with open("enkacard_config.js", "w") as config_js:
            config_js.write("characters = [{}];\nimgdir = \"{}\"\n".format(
                ', '.join(character_list_str), outputdir))

asyncio.run(generate_cards())
