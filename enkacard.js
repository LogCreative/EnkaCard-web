enkacard_object = document.createElement("div")
enkacard_object.setAttribute("id","enkacard")
enkacard_headbar = document.createElement("div")
enkacard_headbar.setAttribute("id","enkacard_headbar")
enkacard_detail = document.createElement("img")
enkacard_detail.setAttribute("id","enkacard_detail")

function showCharacter(e) {
    character_obj = document.getElementById("enkacard_detail")
    character_obj.setAttribute("src", imgdir + "/wide_" + this.id + ".png")
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
