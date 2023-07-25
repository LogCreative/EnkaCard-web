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

function showCharacter(e) {
    character_obj_narrow = document.getElementById("enkacard_detail_narrow")
    character_obj_narrow.setAttribute("srcset", imgdir + "/narrow_" + this.id + ".png")
    character_obj_wide = document.getElementById("enkacard_detail_wide")
    character_obj_wide.setAttribute("srcset", imgdir + "/wide_" + this.id + ".png")
    character_obj_img = document.getElementById("enkacard_detail_img")
    character_obj_img.setAttribute("src", imgdir + "/wide_" + this.id + ".png")
}

characters.forEach(character => {
    chara_img = document.createElement("img")
    chara_img.setAttribute("id",character)
    chara_img.setAttribute("src",`${imgdir}/icon_${character}.png`)
    chara_img.addEventListener('click', showCharacter)
    enkacard_headbar.appendChild(chara_img)
});

enkacard_object.appendChild(enkacard_headbar)
enkacard_object.appendChild(enkacard_detail)
document.getElementsByTagName("enkacard")[0].replaceWith(enkacard_object)
