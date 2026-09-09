function setQuestion(question) {

    const input =
        document.getElementById("homeQuestion");

    if (input) {

        input.value = question;

        input.focus();

    }

}


function askHomeQuestion() {

    const input =
        document.getElementById("homeQuestion");

    if (!input) return;

    const question =
        input.value.trim();

    if (!question) {

        alert("Please enter your question.");

        return;

    }


    localStorage.setItem(
        "smartAssistQuestion",
        question
    );


    window.location.href =
        "pages/assistant.html";

}