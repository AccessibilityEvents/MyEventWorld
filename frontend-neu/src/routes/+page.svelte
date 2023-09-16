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
	let search_results: Event[] = [
		{
			Titel: 'Test',
			Start: '2021-06-01T00:00:00',
			Ende: '2021-06-01T00:00:00',
			Ort: 'Test',
			Link: 'Test',
			Beschreibung: 'Test',
			Preis: 'Test'
		}
	];

	async function search() {
		const response = await fetch(`${BACKEND_SERVER}/api/search?therm=${search_text}`);
		const data = await response.json();
		search_results = data;
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

	{#each search_results as result}
		<article>
			<hgroup>
				<h2>{result.Titel}</h2>
				<h3><a href={result.Link}>{result.Link}</a></h3>
			</hgroup>
			<p>{result.Beschreibung}</p>

			<a href="#" role="button" class="secondary">Anschauen</a>

			<footer>{result.Ort} • {result.Start} • {result.Preis}</footer>
		</article>
	{/each}
</main>
