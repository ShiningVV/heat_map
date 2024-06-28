<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D Image Viewer</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <div>
        <label for="sliceSlider">Slice: </label>
        <input type="range" id="sliceSlider" name="sliceSlider" min="1" max="51" value="1">
    </div>
    <div id="plot"></div>

    <script>
        // Function to load and plot a slice
        async function plotSlice(sliceIndex) {
            const response = await fetch(`data/slice_${sliceIndex}.json`);
            const data = await response.json();
            
            const trace = {
                z: data,
                type: 'heatmap',
                colorscale: 'Gray'
            };
            
            const layout = {
                title: `Slice ${sliceIndex}`,
                xaxis: { title: 'X' },
                yaxis: { title: 'Y' }
            };
            
            Plotly.newPlot('plot', [trace], layout);
        }

        // Initial plot
        plotSlice(1);

        // Update plot on slider change
        document.getElementById('sliceSlider').addEventListener('input', function() {
            plotSlice(this.value);
        });
    </script>
</body>
</html>
