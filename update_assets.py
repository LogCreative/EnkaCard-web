###################################
# Fix enkanetwork_update is not inclueded in the dist of enkacard: v3.3.8
# Upstream should fix this.
import enkacard.enkatools
from EnkaCard.enkacard.src.utils.enkanetwork_update import enka_update
def download_wrapper(self, path):
    return enka_update.dowload(path=path)
enkacard.enkatools.Tools.update_assets = download_wrapper
###################################

from enkacard import encbanner
import asyncio

async def main():
    await encbanner.update()

result = asyncio.run(main()) 

print(result)