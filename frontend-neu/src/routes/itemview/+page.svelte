<script>
	let title = 'fancy titel';
	let description =
		'fancy beschreibung 12111elf!!!!drölf!!!!12221111!!!!12111elf!!!!drölf!!!!12221111!!!!amerik12111elf!!!!drölf!!!!12221111!!!!amerik12111elf!!!!drölf!!!!12221111!!!!amerik12111elf!!!!drölf!!!!12221111!!!!amerik12111elf!!!!drölf!!!!12221111!!!!amerik12111elf!!!!drölf!!!!12221111!!!!amerik12111elf!!!!drölf!!!!12221111!!!!amerik12111elf!!!!drölf!!!!12221111!!!!';
	let link_to_event = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ';
	let time = '19.20.1812';
</script>

<dialog open>
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
