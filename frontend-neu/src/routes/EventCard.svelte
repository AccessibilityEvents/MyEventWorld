<script lang="ts">
	import type { Event } from '$lib/event.ts';
	// import EventCardModal from './EventCardModal.svelte';
	import EuroIcon from '$lib/icons/euro.svelte';
	import MapPinIcon from '$lib/icons/map-pin.svelte';
	import CalendarDaysIcon from '$lib/icons/calendar-days.svelte';
	import GlobeIcon from '$lib/icons/globe.svelte';
	import TagIcon from '$lib/icons/tag.svelte';

	export let event: Event;
</script>

<article>
	<h2>{event.title}</h2>

	<p>{event.description}</p>

	<!-- <EventCardModal title={titel} description={beschreibung} link_to_event={link} time={start} /> -->
	<add-to-calendar-button
		name={event.title}
		description={event.description}
		startDate={event.start_date}
		endDate={event.end_date}
		location={event.location}
		options="['Apple','Google','iCal','Microsoft365','Outlook.com','Yahoo']"
		timeZone="Europe/Berlin"
		trigger="click"
		inline
		listStyle="modal"
		iCalFileName="Reminder-Event"
	/>

	<footer>
		<EuroIcon />
		{event.price} <br />
		<MapPinIcon />
		{event.location} <br />
		<CalendarDaysIcon />
		{event.start_date} <br />
		<TagIcon /> {event.topics.replace(" ", ", ")} <br>

		<GlobeIcon /> <a href={event.link}>{event.link}</a>
	</footer>
</article>
