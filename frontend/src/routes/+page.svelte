<script lang="ts">
	import { onMount } from 'svelte';
	import SettingsIcon from '$lib/icons/settings.svelte';
	import EventCard from './EventCard.svelte';
	import type { Event } from '$lib/event.ts';
	import { PUBLIC_BACKEND_SERVER } from '$env/static/public';

	let search_text: string = '';
	let category: string = '';
	let search_results: Event[] = [];
	let loading: boolean = false;
	let distance: number = 50;

	async function search() {
		loading = true;

		let search_route: string;
		if (search_text === '' && category === '') {
			search_route = 'all';
			console.log('Search All');
		} else {
			search_route = `search?therm=${search_text}&category=${category}`;
			console.log('Search specific');
		}

		const response = await fetch(`${PUBLIC_BACKEND_SERVER}/api/${search_route}`);
		const data = await response.json();

		if (!data.Code) {
			search_results = data;
			console.log(data);
		} else {
			search_results = [];
		}

		loading = false;
	}

	onMount(async () => {
		search();
	});
</script>

<main class="container">
	<div style="display: flex; align-items: baseline; justify-content: space-between;">
		<h1>MyEventWorld</h1>
		<img src="logo.png" alt="Logo" />
	</div>

	<form>
		<div class="grid">
			<div>
				<label for="search">Suche</label>
				<input id="search" type="search" bind:value={search_text} placeholder="Suche" autofocus />
			</div>

			<div>
				<label for="kategoire">Kategorie</label>
				<select name="Kategorie" id="kategorie" bind:value={category}>
					<option>MINT</option>
					<option>Politik</option>
					<option>Bürgerbeteiligung</option>
					<option>Sprache</option>
					<option>Handwerk</option>
					<option>Informatik</option>
					<option>Kunst/Kultur</option>
					<option>Geschichte</option>
					<option>Logikspiele/Spiele</option>
					<option>Sport</option>
					<option>Schule</option>
				</select>
			</div>
		</div>

		<div class="grid">
			<div>
				<label for="ort">Ort</label>
				<input id="ort" type="text" placeholder="Ort eingeben" />
			</div>
			<div>
				<label for="distanz">
					<div style="display: flex; justify-content: space-between;">
						<div>Distanz</div>
						<div>
							{distance} km
						</div>
					</div>
				</label>
				<input bind:value={distance} id="distanz" type="range" min="0" max="100" />
			</div>
		</div>

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
			<EventCard event={result} />
		{/each}
	{/if}
</main>
