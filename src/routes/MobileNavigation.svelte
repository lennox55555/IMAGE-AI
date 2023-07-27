<script>
    import Menu from "$lib/images/menu.png";

    let isToggled = false;


    let backgroundColor = "#252525";

    function toggle() {
        isToggled = !isToggled;


    }
</script>
<img class="burger" src={Menu} on:click={toggle} alt="">

{#if isToggled}

    <div id="sidePanel"></div>
{:else}
    
    <div id="byeSidePanel"></div>
    
{/if}

<style>
    button {
        width: 75px;
        height: 75px;
        border-radius: 25px;
        background-color: #4a4e69;

    }
    .burger {
        width: 50px;
        height: 50px;
        z-index: 3;
        margin-top: 20px;
        margin-left: 20px;

    }

    #sidePanel {
        width: 100%;
        height: 100%;
        background-color: #252525;
        position: absolute;
        z-index: 2;
        animation: slide ease .25s;
    }

    #byeSidePanel {
        width: 100%;
        height: 100%;
        position: absolute;
        animation: slide1 ease .25s;
    }

    @keyframes slide {
        0%{
            opacity: 0.1;
        }
        100% {
           opacity: 1;
        }

    }

    @keyframes slide1 {
        0% {
            opacity: 1;
            background-color: #252525;
        }
        100% {
            opacity: .1;

        }
    }
</style>

