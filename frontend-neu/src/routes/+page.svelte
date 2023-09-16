<script lang="ts">
	import SettingsIcon from '$lib/settings.svelte';

	interface Event {
		Titel: string;
		Start: string;
		Ende: string;
		Ort: string;
		Link: string;
		Beschreibung: string;
		Preis: string;
	}

	const BACKEND_SERVER = 'http://192.168.53.46:5000/';

	let search_text = '';
	let search_results: Event[] = [];

	async function search() {
		const response = await fetch(`${BACKEND_SERVER}/api/all?therm=${search_text}`);
		const data = await response.json();
		search_results = data;
	}
</script>

<main class="container">
	<h1>MyEventWorld</h1>

	<input type="search" bind:value={search_text} placeholder="Suche" />
	<a href="/sidebar">
		<button style="width: 10%;" class="outline">
			<SettingsIcon />
		</button>
	</a>

	<button on:click={search}>Suchen</button>

	{#each search_results as result}
		<article>
			<h2><a href="#">{result.Titel}</a></h2>

			<p>{result.Beschreibung}</p>

			<footer>
				<p>
					{result.Ort} • {result.Start} • {result.Preis} <br />

					<a href={result.Link}>{result.Link}</a>
				</p>
			</footer>
		</article>
	{/each}
</main>
