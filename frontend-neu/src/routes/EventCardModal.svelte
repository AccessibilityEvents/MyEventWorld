<script lang="ts">
	export let title: string;
	export let description: string;
	export let link_to_event: string;
	export let time: string;
</script>

<button class="secondary" data-target={title} onClick="toggleModal(event)">Anschauen</button>

<dialog id={title}>
	<article>
		<header>
			<a href="#close" aria-label="Close" class="close" />
			<h3>
				{title}
				<h3 />
			</h3>
		</header>
		<p>
			{description}
		</p>
		<footer>
			<a href={link_to_event}>Link zu der:dem Veranstalter:in</a>
			<p class="primary">{time}</p>
		</footer>
	</article>
</dialog>

<style>
	article footer {
		text-align: left;
	}
</style>
