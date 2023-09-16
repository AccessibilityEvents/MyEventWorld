<script lang="ts">
    export let titel: string;
    export let beschreibung: string;
    export let ort: string;
    export let start: string;
    export let preis: string;
    export let link: string;

</script>

<article>
    <h2><a href="#">{titel}</a></h2>

    <p>{beschreibung}</p>

    <footer>
        <p>
            {ort} • {start} • {preis} <br />

            <a href={link}>{link}</a>
        </p>
    </footer>
</article>
