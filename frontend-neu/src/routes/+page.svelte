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

	async function search() {
		loading = true;

		let search_route: string;
		if (search_text === "") {
			search_route = "all";
		} else {
			search_route = `search?therm=${search_text}`
		}

		const response = await fetch(`${BACKEND_SERVER}/api/${search_route}`);
		const data = await response.json();

		if (!data.Code) {
			search_results = data;
		} else {
			search_results = [];
		}

		loading = false;
	}

	// onMount(async () => { search()});
</script>

<main class="container">
	<h1>MyEventWorld</h1>

	<form>
		<input type="search" bind:value={search_text} placeholder="Suche" autofocus/>
<!--
		<a href="/settings">
			<button style="width: 10%;" class="outline">
				<SettingsIcon />
			</button>
		</a> -->

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
