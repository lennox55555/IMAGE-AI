<script>
    import BarChart from '/Users/lennox/Documents/Webstorm/ReactiveWebsite/ReactiveWebsite/myapp/src/BarChart.svelte';

    let chartData = [
        { label: 'A', value: 10 },
        { label: 'B', value: 20 },
        { label: 'C', value: 15 },
        { label: 'D', value: 8 },
        { label: 'E', value: 40 },
    ];

    // Assign the chartData to the 'data' variable
    let data = chartData;

    let num = 0;

    function handleChange(event) {
        num = Number(event.target.value);
    }
</script>



<div class="container">
    <input class="input-field" type="number" bind:value={num} on:input={handleChange} />
</div>


<BarChart {data} width={500} height={300} margin={{ top: 20, right: 20, bottom: 30, left: 40 }} />
