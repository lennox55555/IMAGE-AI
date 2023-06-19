
    {#if showDivs}
        <div transition:fade class="container">
            <!--<button class="start-btn" on:click={handleButtonClick}>Start Visualizing</button>!-->
            <div class="small-circle" style="top: {(yvalue+4200)/7+'px'}; left: {(xvalue+1300)/7+'px'}"></div>
            <div class="small-circle" style="top: {(yvalue+2500)/6+'px'}; left: {(xvalue+500)/6+'px'}"></div>
            <div class="small-circle" style="top: {(yvalue+900)/5+'px'}; left: {(xvalue+500)/5+'px'}"></div>
            <div class="small-circle" style="top: {(yvalue+900)/7+'px'}; left: {(xvalue+2900)/7+'px'}" ></div>
            <div class="small-circle" style="top: {(yvalue+2000)/6+'px'}; left: {(xvalue+4200)/6+'px'}"></div>
            <div class="medium-circle" style="top: {(yvalue)+'px'}; left: {(xvalue-100)+'px'}"></div>
            <div class="medium-circle" style="top: {(yvalue+1300)/3+'px'}; left: {(xvalue+900)/3+'px'}" ></div>
            <div class="medium-circle" style="top: {(yvalue+200)/2+'px'}; left: {(xvalue+300)/2+'px'}" ></div>
            <div class="medium-circle" style="top: {(yvalue+100)+'px'}; left: {(xvalue+550)+'px'}" ></div>

        </div>
    {/if}



<div id="hero">
    <div id="circle-bg">
        <img  id="professionalPicture" src="./src/images/ProfessionalPicture.jpg">
    </div>
    <div id="hero-text">
        {#if visible}
            <h2 class="heroText-a" transition:typewriter>
                Hi, I'm Lennox,
            </h2>
            <h1 class="heroText-b" transition:typewriter>
                Software Developer
            </h1>
            <p class="heroText-c" transition:typewriter>
                Based in Boulder, Colorado
            </p>
        {/if}
    </div>
</div>



<style>

    .heroText-a {
        font-family: 'Heebo', sans-serif;
        font-weight: lighter;
    }

    .heroText-b {
        font-family: 'Heebo', sans-serif;
    }

    .heroText-c {
        font-family: 'Heebo', sans-serif;
        font-weight: lighter;
    }

    #hero-text {
        display: block;
        margin-top: 25px;
        margin-left: 10px;
    }

    .small-circle {
        width: 300px;
        height: 300px;
        background-color: #E8375D;
        border-radius: 50px;
        position: absolute;
        opacity: .7;
        z-index: -1;


    }

    .medium-circle {
        width: 500px;
        height: 500px;
        background-color: #736CED;
        border-radius: 50px;
        position: absolute;
        top: 75%;
        left: 65%;
        opacity: .8;
        z-index: -1;
    }

    @keyframes float {
        0%{}
        20%{transform: translateY(20px);}
        40%{transform: translateY(-20px);}
        60%{transform: translateX(-20px);}
        80%{transform: translateX(20px);}


    }

    #professionalPicture {
        height: 200px;
        width: 200px;
        border-radius: 120px;
        margin: auto;
    }

    #circle-bg {
        height: 220px;
        width: 220px;
        background: white;
        border-radius: 130px;
        top: 30%;
        right: 50%;
        margin: auto;
        display: flex;
        justify-content: center;
        align-items: center;

    }

    #hero {
        position: absolute;
        top: 30%;
        left: 30%;
        display: flex;
    }

</style>




<script>
    import { fade } from 'svelte/transition';

    export let yvalue = 0;
    export let xvalue = 0;

    let showDivs = true;
    window.addEventListener('mousemove', function (e) {
        yvalue = e.y / 5
        xvalue = e.x / 5
        console.log(`y: ${e.y}`)
        console.log(yvalue)


        if (yvalue > 150) {
            showDivs = false;
        }
        else if (yvalue < 150) {
            showDivs = true
        }

    })

    let visible = true;


    function typewriter(node, { speed = 5 }) {
        const valid = (
            node.childNodes.length === 1 &&
            node.childNodes[0].nodeType === Node.TEXT_NODE
        );

        if (!valid) {
            throw new Error(`This transition only works on elements with a single text node child`);
        }

        const text = node.textContent;
        const duration = text.length / (speed * 0.01);

        return {
            duration,
            tick: t => {
                const i = Math.trunc(text.length * t);
                node.textContent = text.slice(0, i);
            }
        };
    }


</script>

