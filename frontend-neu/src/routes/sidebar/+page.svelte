<script>
	//import { onMount, reactive } from "svelte";
	let ort = '';
	let distanz = 0;
	// let filter = reactive({});

	const updateFilter = (event) => {
		filter[event.target.name] = event.target.checked;
	};

	// onMount(async () => {
	//     map = new google.maps.Map(document.getElementById("map"), {
	//       center: { lat: -34.397, lng: 150.644 },
	//       zoom: 8,
	//     });
	//  });
</script>

<main class="container">
	<div>
		<label for="ort">Ort:</label>
		<input id="ort" bind:value={ort} type="text" placeholder="Ort eingeben" />
	</div>

	<div>
		<label for="distanz">Distanz:</label>
		<input id="distanz" bind:value={distanz} type="range" min="0" max="100" />
	</div>

	<div>
		<h2>Filter für Veranstaltungen</h2>
		<label>
			<input type="checkbox" name="filter1" on:change={updateFilter} />
			Filter1
		</label>
		<label>
			<input type="checkbox" name="filter2" on:change={updateFilter} />
			Filter2
		</label>
	</div>
</main>

<style>
	#map {
		height: 300px;
		width: 100%;
	}
</style>
