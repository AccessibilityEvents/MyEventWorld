<script lang="ts">
	// import EventCardModal from './EventCardModal.svelte';
	import EuroIcon from '$lib/icons/euro.svelte';
	import MapPinIcon from '$lib/icons/map-pin.svelte';
	import CalendarDaysIcon from '$lib/icons/calendar-days.svelte';
	import GlobeIcon from '$lib/icons/globe.svelte';

	export let titel: string;
	export let beschreibung: string;
	export let ort: string;
	export let start: string;
	export let preis: string;
	export let link: string;
</script>

<article>
	<h2>{titel}</h2>

	<p>{beschreibung}</p>

	<!-- <EventCardModal title={titel} description={beschreibung} link_to_event={link} time={start} /> -->

	<footer>
		<EuroIcon />
		{preis} <br />
		<MapPinIcon />
		{ort} <br />
		<CalendarDaysIcon />
		{start} <br />

		<GlobeIcon /> <a href={link}>{link}</a>
	</footer>
</article>
