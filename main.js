let addButton = document.getElementById("addToDoList");
let container = document.getElementById("toDoContainer");
var inputField = document.getElementById("inputField");

addButton.addEventListener('click', function(){
    let node = document.createElement("li")
    let removeBt = document.createElement("button")
    removeBt.innerHTML = "Remove"
    let textnode = document.createTextNode(inputField.value)
    node.appendChild(textnode)

    node.appendChild(removeBt)
    document.getElementById("toDoContainer").appendChild(node)

    removeBt.addEventListener('click', ()=>{
        node.remove();
      })

})