<script>
	import SettingsIcon from '$lib/settings.svelte';

	const BACKEND_SERVER = "http://localhost:5000/"

	let search_text = '';

	async function search() {

	}
</script>

<main class="container">
	<h1>MyEventWorld</h1>

	<input type="search" bind:value={search_text} />
	<a href="/sidebar">
		<button style="width: 10%;" class="outline">
			<SettingsIcon />
		</button>
	</a>

	<button on:click={search}>Suchen</button>

</main>
