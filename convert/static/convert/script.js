document.addEventListener('DOMContentLoaded', function() {
    const convert = document.getElementById('convert');
    const chart = document.getElementById('chart');
    const convertView = document.getElementById('convert-view');
    const chartView = document.getElementById('chart-view');
    const convertText = document.getElementById('convert-text');
    const chartText = document.getElementById('chart-text');

    convert.addEventListener('click', function() {
        convertView.classList.remove('hidden');
        chartView.classList.add('hidden');
        convertText.classList.remove('hidden');
        chartText.classList.add('hidden');
    });

    chart.addEventListener('click', function() {
        chartView.classList.remove('hidden');
        convertView.classList.add('hidden');
        convertText.classList.add('hidden');
        chartText.classList.remove('hidden');
    });

});