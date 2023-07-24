<script>
    import { onMount } from "svelte";

    let currentLineIndex = 0;
    let currentText = '';
    let currentIndex = 0;
    let typingSpeed = 50;
    let isTyping = true;

    onMount(() => {
        typeNextCharacter();
    });

    function typeNextCharacter() {
        if (currentLineIndex >= lines.length) {
            isTyping = false;
            return;
        }

        if (currentIndex < lines[currentLineIndex].length) {
            currentText += lines[currentLineIndex][currentIndex];
            currentIndex++;
            setTimeout(typeNextCharacter, typingSpeed);
        } else {
            currentText += "\n"; // Add a new line after each line
            currentLineIndex++;
            if (currentLineIndex < lines.length) {
                currentIndex = 0;
                setTimeout(typeNextCharacter, 1000); // Pause for 1 second between lines
            }
        }
    }




    let inputValue = "";
    let inputWidth = "35px";

    let lines = [
        ">",
        "Hello, my name is Lennox Anderson",
        "I am based in Denver Colorado",

    ];

    function handleKeyDown(event) {

        inputWidth = inputValue.length * 2;
    }

    // Add event listener when the component is mounted
    onMount(() => {
        window.addEventListener("keydown", handleKeyDown);
    });



</script>

<svelte:head>
    <title>Home</title>
    <meta name="description" content="Home Page" />
</svelte:head>

<div id="terminalBorder">
    <div id="terminalBackground">
        <p class="terminalText">{currentText}</p>
        <div id="terminalLayout" >
            <p id="terminalCode">> {inputValue}</p>
            <input bind:value={inputValue} style="width: {inputWidth}"/>

            <div id="inputBlink"><p></p></div>
        </div>
    </div>
</div>


<style>

    #terminalBorder {
        width: 80%;
        height: 90%;
        background-color: #010000;
        margin: auto;
        border-radius: 20px;
        padding-top: 20px;
    }

    #terminalBackground {
        width: 100%;
        height: 100%;
        background-color: #252525;
        margin: auto;
        border-bottom-right-radius: 20px;
        border-bottom-left-radius: 20px;
    }

    #terminalCode {
        color: white;
        font-family: 'MyCustomFont', sans-serif;
        font-weight: bold;
        padding: 8px 10px;
        position: relative;
        bottom: 20px;
    }

    #terminalLayout {
        display: flex;
    }

    input {

        background-color: transparent;
        color: white;
        font-family: 'MyCustomFont', sans-serif;
        font-weight: bold;
        height: 20px;
        caret-color: transparent;
        margin-left: 10px;
        z-index: 2;
        position: relative;
        border: none;
        outline: none;
        box-shadow: none;

    }



    #inputBlink {
        animation: blink 1.15s linear infinite;
        background-color: white;
        width: 12px;
        color: white;
        height: 26px;
        z-index: 1;
        right: 25px;
        position: relative;
    }

    .terminalText {
        color: white;
        font-family: 'MyCustomFont', sans-serif;
        padding: 8px 10px;
    }

    @keyframes blink  {
        0% { opacity: 1; }
        49% { opacity: 1; }
        50% { opacity: 0; }
        100% { opacity: 0; }
    }
</style>
