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
	let loading: boolean = false;
	let input_error: boolean = false;

	async function search() {
		if (search_text === "") {
			input_error = true;
			return
		}

		input_error = false;
		loading = true;

		const response = await fetch(`${BACKEND_SERVER}/api/search?therm=${search_text}`);
		const data = await response.json();
		search_results = data;

		loading = false;
	}

	onMount(async () => {
		loading = true;

		const response = await fetch(`${BACKEND_SERVER}/api/all`);
		const data = await response.json();
		search_results = data;

		loading = false;
	});
</script>

<main class="container">
	<h1>MyEventWorld</h1>

	<form>
		{#if input_error}
			<input type="search" aria-invalid="true" bind:value={search_text} placeholder="Suche" autofocus/>
		{:else}
			<input type="search" bind:value={search_text} placeholder="Suche" autofocus/>
		{/if}

		<a href="/settings">
			<button style="width: 10%;" class="outline">
				<SettingsIcon />
			</button>
		</a>

		{#if !loading}
			<button type="submit" on:click|preventDefault={search}>Suchen</button>
		{:else}
			<button type="submit" disabled>Suchen</button>
		{/if}
	</form>

	{#if loading}
		<h1 aria-busy="true" />
	{:else}
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
	{/if}
</main>
