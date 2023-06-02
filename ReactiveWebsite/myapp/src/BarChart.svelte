<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';

    export let data;
    export let width = 500;
    export let height = 300;
    export let margin = { top: 20, right: 20, bottom: 30, left: 40 };

    let svg;
    let xScale;
    let yScale;

    onMount(() => {
        const svgWidth = width - margin.left - margin.right;
        const svgHeight = height - margin.top - margin.bottom;

        svg = d3.select('#chart')
            .append('svg')
            .attr('width', width)
            .attr('height', height)
            .append('g')
            .attr('transform', `translate(${margin.left},${margin.top})`);

        xScale = d3.scaleBand()
            .range([0, svgWidth])
            .padding(0.1)
            .domain(data.map(d => d.label));

        yScale = d3.scaleLinear()
            .range([svgHeight, 0])
            .domain([0, d3.max(data, d => d.value)]);

        svg.selectAll('.bar')
            .data(data)
            .enter()
            .append('rect')
            .attr('class', 'bar')
            .attr('x', d => xScale(d.label))
            .attr('y', d => yScale(d.value))
            .attr('width', xScale.bandwidth())
            .attr('height', d => svgHeight - yScale(d.value));

        svg.append('g')
            .attr('class', 'x-axis')
            .attr('transform', `translate(0,${svgHeight})`)
            .call(d3.axisBottom(xScale));

        svg.append('g')
            .attr('class', 'y-axis')
            .call(d3.axisLeft(yScale));
    });
</script>

<style>
    .bar {
        fill: steelblue;
    }

    .x-axis text {
        font-size: 12px;
    }

    .y-axis text {
        font-size: 12px;
    }
</style>

<div id="chart"></div>
