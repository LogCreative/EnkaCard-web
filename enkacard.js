enkacard_object = document.createElement("div")
enkacard_object.setAttribute("id","enkacard")
enkacard_headbar = document.createElement("div")
enkacard_headbar.setAttribute("id","enkacard_headbar")
enkacard_detail = document.createElement("picture")
enkacard_detail.setAttribute("id","enkacard_detail")
enkacard_detail_narrow = document.createElement("source")
enkacard_detail_narrow.setAttribute("media", "(max-width: 599px)")
enkacard_detail_narrow.setAttribute("width", "100%")
enkacard_detail_narrow.setAttribute("id", "enkacard_detail_narrow")
enkacard_detail_wide = document.createElement("source")
enkacard_detail_wide.setAttribute("media", "(min-width: 600px)")
enkacard_detail_wide.setAttribute("id", "enkacard_detail_wide")
enkacard_detail_img = document.createElement("img")
enkacard_detail_img.setAttribute("id", "enkacard_detail_img")
enkacard_detail.appendChild(enkacard_detail_narrow)
enkacard_detail.appendChild(enkacard_detail_wide)
enkacard_detail.appendChild(enkacard_detail_img)

chara_img_list = []

function showCharacter(e) {
    chara_img_list.forEach(element => {
        element_chara_rarity = element.id.split('-')[1]
        element.classList.remove("rarity" + element_chara_rarity)
    });
    chara_rarity = this.id.split('-')[1]
    this.classList.add("rarity" + chara_rarity)
    character_obj_narrow = document.getElementById("enkacard_detail_narrow")
    character_obj_narrow.setAttribute("srcset", imgdir + "/narrow-" + this.id + ".jpg")
    character_obj_wide = document.getElementById("enkacard_detail_wide")
    character_obj_wide.setAttribute("srcset", imgdir + "/wide-" + this.id + ".jpg")
    character_obj_img = document.getElementById("enkacard_detail_img")
    character_obj_img.setAttribute("src", imgdir + "/wide-" + this.id + ".jpg")
}

characters.forEach(character => {
    chara_div = document.createElement("div")
    chara_div.setAttribute("class", "imgdiv")
    chara_img = document.createElement("img")
    chara_img.setAttribute("id",character)
    chara_img.setAttribute("src",`${imgdir}/avatar-${character}.png`)
    chara_img.addEventListener('click', showCharacter)
    chara_img_list.push(chara_img)
    chara_div.appendChild(chara_img)
    enkacard_headbar.appendChild(chara_div)
});

enkacard_object.appendChild(enkacard_headbar)
enkacard_object.appendChild(enkacard_detail)
document.getElementsByTagName("enkacard")[0].replaceWith(enkacard_object)
chara_img_list[0].click()
