function checkText() {
    let txtArea = document.getElementById('textarea');
    let code_r = '<code style="background-color: #242322; color: white; font-size: 17px; padding-right: 2px;">//write your code here </code>';
    let quit_r = '<p style="padding=0px; margin=0px">  </p>'
    let quote_r = '<q style="font-style:italic; font-size: 17px; background-color: #181a18"> write your quote here '
    let tags = [':code', ':quote', ':quit'];

    for(let i = 0 ; i < tags.length ; i++){
        let tag = tags[i];
        let varName = tag.substring(1) + '_r'
        if (txtArea.innerHTML.includes(tag)) {
            txtArea.innerHTML = txtArea.innerHTML.replace(tag, eval(varName));
        }
    }

}
function handleTab(event) {
    if (event.key === 'Tab') {
        event.preventDefault();
        document.execCommand('insertHTML', false, '&#32;&#32;&#32;&#32;');
    }
}