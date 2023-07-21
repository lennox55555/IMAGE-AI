<script>
	import Book from "$lib/images/book.png"
	import Code from "$lib/images/code.png"
	import User from "$lib/images/user.png"
	import Home from "$lib/images/home.png"

</script>

<nav>

	<ul>
		<li><a href="/"><img alt="Book Icon" class="icon" src={Home}>Home</a></li>
		<li><a href="/about"><img alt="Book Icon" class="icon" src={User}>About</a></li>
		<li><a href="/independentResearch"><img alt="Book Icon" class="icon" src={Book}>Independent Research</a></li>
		<li><a href="/portfolio"><img alt="Book Icon" class="icon" src={Code}>Portfolio</a></li>
	</ul>
</nav>

<style>

	nav {
		background-color: #22223b;
		width: 50%;

	}
	ul {
		align-content: space-evenly;
		display: flex;
		list-style: none;
		justify-content: center;
	}
	li {
		margin-right: 2rem;
		font-family: 'MyCustomFont', sans-serif;
	}

	a {
		text-decoration: none;
		color: #adb5bd;
	}
	.icon {
		width: 20px;
		padding-right: 8px;

	}

	@font-face {
		font-family: 'MyCustomFont';
		src: url('src/lib/fonts/NotoSansMono-VariableFont_wdth,wght.ttf') format('woff'),
		url('src/lib/fonts/NotoSansMono-VariableFont_wdth,wght.ttf') format('truetype');
	}


</style>
