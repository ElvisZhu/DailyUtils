#http://tonkiang.us/hotellist.html
rs = document.querySelectorAll('div.result')
var s = '#EXTM3U'; 
for (let i = 0; i < rs.length; i++) {
    if (rs[i].children.length>1) {
        var name= rs[i].children[0].innerText.replaceAll('\t','').replaceAll('\n','')
        var m3u8 = rs[i].children[1].innerText.replaceAll('\t','').replaceAll('\n','')
        if (name!='') {
            s = s+'\n#EXTINF:0,'+name+'\n'+m3u8
        }
    }
}
console.log(s)
