const addBtn = document.querySelector(".add-btn"),
wrapper = document.querySelector(".wrapper"),
closeBtn = document.querySelector(".close-btn"),
editBtn = document.querySelectorAll(".edit");

addBtn.addEventListener("click",()=>{
    wrapper.style.display="initial";
    document.getElementById("noteForm").action = "/add";
    wrapper.querySelector("#textBox").value = "";
    wrapper.querySelector("#edit_content").value = "";
    wrapper.querySelector("#note_id").value = "";
});

closeBtn.addEventListener("click",()=>{
    wrapper.style.display="none";
});

editBtn.forEach(edit => {
    edit.addEventListener("click",(e)=>{
        e.preventDefault();
        const card = edit.closest(".card");
        const title = card.querySelector(".card_title").innerText;
        const content = card.querySelector(".content").innerText;
        const noteId = edit.getAttribute("data-id");

        wrapper.style.display="initial"
        wrapper.querySelector("#textBox").value = title;
        wrapper.querySelector("#edit_content").value = content;
        wrapper.querySelector("#note_id").value = noteId;

        document.getElementById("noteForm").action = `/edit/${noteId}`;
    });
});



