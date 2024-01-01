var textarea = document.getElementById("textarea");

function Tsave(){
    var content = textarea.innerHTML;
    localStorage.setItem("quickNote", content)
}

textarea.addEventListener("input", function(){
    Tsave();
    checkText();
})

function Tload(){
    var content = localStorage.getItem("quickNote")
    if (content){
        textarea.innerHTML = content;
    }
}

window.addEventListener("load", function(){
    Tload();
    checkText();
})

function checkText() {
    let txtArea = document.getElementById('textarea');
    let code_r = '<code style="background-color: #242322; color: white; font-size: 17px; padding: 2px;">//write your code here </code>';
    let quit_r = '<p style="padding:0px; margin:0px">  </p>'
    let quote_r = '<q style="font-style:italic; font-size: 17px; background-color: #181a18"> write your quote here '
    let tags = [':code', ':quote', ':quit'];

    for(let i = 0 ; i < tags.length ; i++){
        let tag = tags[i];
        let varName = tag.substring(1) + '_r'
        if (txtArea.innerText.includes(tag)) {
            txtArea.innerHTML = txtArea.innerHTML.replace(tag, eval(varName));
        }
    }
}
function handleTab(event) {
    if (event.key === 'Tab') {
        event.preventDefault();
        document.execCommand('insertHTML', false, '&nbsp;&nbsp;&nbsp;&nbsp;');
    }
}

// board (sticky notes part)
const note_container = document.getElementById("app");
const add_note_buttom = document.querySelector("add-note");

function getNote(){
    // using flask 
}

function saveNote(){
    // using flask 
}

function createNote(id, content){
    const element = document.createElement("textarea");
    element.classList.add("node");
    element.placeholder = "tap here...";
    element.value = content

    element.addEventListener("change", () => {
        updateNote(id, element.value);
    });

    element.addEventListener("dblclick", () => {
        const doDelete = confirm("are you sure you wish to delete this note?")
        if (doDelete){
            deleteNote(id, content)
        }
    });

    return element;
}

function addNote(){

}

function updateNote(){

}
