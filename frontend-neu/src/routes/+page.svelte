<script lang="ts">
	import { onMount } from 'svelte';
	import SettingsIcon from '$lib/settings.svelte';
	import EventCard from './EventCard.svelte';

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
		if (search_text === '') {
			return;
		}
		const response = await fetch(`${BACKEND_SERVER}/api/search?therm=${search_text}`);
		const data = await response.json();
		search_results = data;
	}

	onMount(async () => {
		const response = await fetch(`${BACKEND_SERVER}/api/all`);
		const data = await response.json();
		search_results = data;
	});
</script>

<main class="container">
	<h1>MyEventWorld</h1>

	<form>
		<input type="search" bind:value={search_text} placeholder="Suche" />
		<a href="/sidebar">
			<button style="width: 10%;" class="outline">
				<SettingsIcon />
			</button>
		</a>
		<button type="submit" on:click={search}>Suchen</button>
	</form>

	{#each search_results as result}
		<EventCard
			titel={result.Titel}
			beschreibung={result.Beschreibung}
			ort={result.Ort}
			start={result.Start}
			preis={result.Preis}
			link={result.Link}
		/>
	{/each}
</main>
