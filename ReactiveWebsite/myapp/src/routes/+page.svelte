{#if showDivs}
    <div transition:fade class="container">
        <!--<button class="start-btn" on:click={handleButtonClick}>Start Visualizing</button>!-->
        <div class="small-circle" style="top: {(yvalue+4200)/7+'px'}; left: {(xvalue+1300)/7+'px'}"></div>
        <div class="small-circle" style="top: {(yvalue+2500)/6+'px'}; left: {(xvalue+500)/6+'px'}"></div>
        <div class="small-circle" style="top: {(yvalue+900)/5+'px'}; left: {(xvalue+500)/5+'px'}"></div>
        <div class="small-circle" style="top: {(yvalue+900)/7+'px'}; left: {(xvalue+2900)/7+'px'}" ></div>
        <div class="small-circle" style="top: {(yvalue+2000)/6+'px'}; left: {(xvalue+4200)/6+'px'}"></div>
        <div class="small-circle" style="top: {(yvalue+600)/5+'px'}; left: {(xvalue+5500)/5+'px'}" ></div>
        <div class="small-circle" style="top: {(yvalue+3600)/6+'px'}; left: {(xvalue+4700)/6+'px'}"></div>
        <div class="small-circle" style="top: {(yvalue+600)/5+'px'}; left: {(xvalue+4500)/5+'px'}" ></div>
        <div class="medium-circle" style="top: {(yvalue+25)+'px'}; left: {(xvalue-100)+'px'}"></div>
        <div class="medium-circle" style="top: {(yvalue+1300)/3+'px'}; left: {(xvalue+1000)/3+'px'}" ></div>
        <div class="medium-circle" style="top: {(yvalue+600)/2+'px'}; left: {(xvalue+1800)/2+'px'}" ></div>
        <div class="medium-circle" style="top: {(yvalue-300)+'px'}; left: {(xvalue+550)+'px'}" ></div>
        <div class="medium-circle" style="top: {(yvalue-100)/3+'px'}; left: {(xvalue+100)/3+'px'}"></div>
        <div class="medium-circle" style="top: {(yvalue-450)/2+'px'}; left: {(xvalue+900)/2+'px'}"></div>
        <div class="medium-circle" style="top: {(yvalue-400)+'px'}; left: {(xvalue+1000)+'px'}"></div>
    </div>
{/if}




    <style>

    .small-circle {
        width: 75px;
        height: 75px;
        background-color: #E8375D;
        border-radius: 50px;
        position: absolute;
        opacity: .7;
        animation: float infinite 9s;

    }

    .medium-circle {
        width: 100px;
        height: 100px;
        background-color: #736CED;
        border-radius: 50px;
        position: relative;
        top: 75%;
        left: 65%;
        animation: float infinite 9s;
        opacity: .8;
    }

    @keyframes float {
        0%{}
        20%{transform: translateY(20px);}
        40%{transform: translateY(-20px);}
        60%{transform: translateX(-20px);}
        80%{transform: translateX(20px);}


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



</script>

