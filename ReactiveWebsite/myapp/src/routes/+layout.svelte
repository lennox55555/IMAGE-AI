<h2 id="title">Lennox Anderson</h2>
<nav class="navbar">
    <a href="/">home</a>
    <a href="/projects">projects</a>
    <a href="/about">about</a>
</nav>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Public+Sans:ital,wght@1,700&display=swap');

    #title {
        position: fixed;
        top: -8px;
        font-family: 'Public Sans', sans-serif;
    }

    .navbar {
        border: #E5E4E2;
        border-bottom-style: solid;
        border-bottom-width: 1px;
        margin-top: 15px;
        padding-bottom: 15px;
        text-align: center;

    }

    .navbar a {
        text-decoration: none;
        color: black;
        font-family: Charter,monospace;
        padding-right: 4%;
    }

    .navbar a:hover {
        text-decoration: underline #252627;
    }

    .background {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
        z-index: -1;
        background-color: #E5E4E2;

    }



    .text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 24px;
        color: #ffffff;
        text-align: center;
    }
</style>

<div class="background"></div>


<slot />

<script>
    import { onMount } from 'svelte';

    let animationClass = '';

    onMount(() => {
        // Trigger animation after the component is mounted
        animationClass = 'animate';
    });
</script>
