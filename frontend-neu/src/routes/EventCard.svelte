<script lang="ts">
	import type { Event } from '$lib/event.ts';
	// import EventCardModal from './EventCardModal.svelte';
	import EuroIcon from '$lib/icons/euro.svelte';
	import MapPinIcon from '$lib/icons/map-pin.svelte';
	import CalendarDaysIcon from '$lib/icons/calendar-days.svelte';
	import GlobeIcon from '$lib/icons/globe.svelte';

	export let event: Event;
</script>

<article>
	<h2>{event.Titel}</h2>

	<p>{event.Beschreibung}</p>

	<!-- <EventCardModal title={titel} description={beschreibung} link_to_event={link} time={start} /> -->
	<add-to-calendar-button
		name="{event.Titel}"
		description="{event.Beschreibung}"
		startDate="{event.Start}"
		endDate="{event.Ende}"
		location="{event.Ort}"
		options="['Apple','Google','iCal','Microsoft365','Outlook.com','Yahoo']"
		timeZone="Europe/Berlin"
		trigger="click"
		inline
		listStyle="modal"
		iCalFileName="Reminder-Event"
	/>

	<footer>
		<EuroIcon />
		{event.Preis} <br />
		<MapPinIcon />
		{event.Ort} <br />
		<CalendarDaysIcon />
		{event.Start} <br />

		<GlobeIcon /> <a href={event.Link}>{event.Link}</a>
	</footer>
</article>
