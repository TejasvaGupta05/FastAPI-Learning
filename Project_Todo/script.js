console.log("HARAMI")

const validURL = "http://127.0.0.1:8000/";

async function updateConnectionStatus() {
    try {
        const response = await fetch(validURL, { method: "GET" });
        const data = await response.json();
        document.getElementById("connectionremark").innerHTML = `<h4 style="color: green;">${data.message || "CONNECTED"}</h4>`;
    } catch (error) {
        document.getElementById("connectionremark").innerHTML = `<h4 style="color: orange;">Connection Failed...Reconnecting</h4>`;
        console.error("Fetch error:", error);
    }
}
updateConnectionStatus();
setInterval(updateConnectionStatus, 3000);

async function fetchtodoscount() {
    try {
        const response = await fetch(validURL+"count",{method:"GET"})
        const data = await response.json()
        document.getElementById("Todoscount").innerText = `No of Todos : ${data["count"]}`;
    } catch (error) {
        console.log(error);
    }
}
fetchtodoscount()

function checkStatus(bool){
    if(bool==true) return "Completed";
    return "Pending";
}

document.getElementById("AddTodoButton").addEventListener("click", async function () {
    let tobeAdded = document.getElementById("InputAddTodo").value;
    if(tobeAdded == ""){
        alert("Field is Empty");
        return;
    }
    // Since URL is http://127.0.0.1:8000/post

    // ? FOR JSON BODY as Request
    // const response = await fetch(validURL+"post",{
    //     method: "POST",
    //     headers: {
    //         "Content-Type" : "application/json"
    //     },
    //     body : JSON.stringify({
    //         title : tobeAdded
    //     })
    // });


    // ? For Query Params as Request e.g. https://url.com/post?title=TASK1
    const response = await fetch(validURL+"post?title="+`${encodeURIComponent(tobeAdded)}`,
        {
            method : "POST"
        }
    );
    // console.log(response);
    const data = await response.json();
    // console.log(data);
    fetchtodoscount();
})

async function findtodo() {
    const id = Number(document.getElementById("InputFindTodo").value);
    if(!Number.isInteger(id)){
        alert("Not a valid ID");
        return;
    }
    const response = await fetch(validURL+"todos/"+`${id}`,{
        method: "GET"
    })
    const data = await response.json();
    // console.log(data);
    try{
        document.getElementById("FindTodoDiv").innerHTML = `
        Title : ${data.Todo.title} <br>
        Status : ${checkStatus(data.Todo.isdone)} <br>
        <div style="display: flex;">
        <button id="markdone">Mark Completed</button><button id="Delete">Delete</button>
        </div>
        `;
        document.getElementById("markdone").addEventListener("click", async function () {
            const response = await fetch(validURL + `mark/${id}`, {
                method: "PUT"
            })
            const data = await response.json();
            findtodo();
        })
        document.getElementById("Delete").addEventListener("click",async function () {
            const response = await fetch(validURL + `delete/${id}`,{
                method : "DELETE"
            })
            const data = await response.json();
            findtodo();
            fetchtodoscount();
        })
    } catch{
        document.getElementById("FindTodoDiv").innerHTML = `NOT FOUND`;
    }
}
document.getElementById("FindTodoButton").addEventListener("click",findtodo);

document.getElementById("fetchall").addEventListener("click",async function () {
    const response = await fetch(validURL+"todos",{
        method : "GET"
    })
    const data = await response.json();
    document.getElementById("Table").innerHTML=`
        <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Is Completed</th>
        </tr>
        <tbody id="TableBody">
        </tbody>`;
    console.log(data);
    let TableBody = document.getElementById("TableBody");
    for (let i = 0; i < data.length; i++) {
        const element = data[i];
        TableBody.insertAdjacentHTML("beforeend",`
            <tr>
                <td>${element.id}</td>
                <td>${element.title}</td>
                <td>${element.isdone}</td>
            </tr>    
        `)
    }
})