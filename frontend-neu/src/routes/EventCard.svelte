<script lang="ts">
	import EventCardModal from './EventCardModal.svelte';

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
		<p>
			{ort} • {start} • {preis} <br />

			<a href={link}>{link}</a>
		</p>
	</footer>
</article>
