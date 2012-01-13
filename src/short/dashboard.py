# -*- coding: utf-8 -*-
from models import Url

def grafico():

    urls = Url.objects.all().order_by('-numero_visitas')[:10]
    html = u"""
    <script type="text/javascript" src="http://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load('visualization', '1', {packages: ['corechart']});
    </script>
    <style>
        .dashboard-module-content{
            background: #fffff4 !important;
        }
    </style>
    <script type="text/javascript">
      function drawVisualization() {
        // Create and populate the data table.
        var data = new google.visualization.DataTable();
        var raw_data = ["""
    for url in urls:
        html += "['%s', %s]," % (url.url, url.numero_visitas)
    html += """];

        var years = ['Mais visitados'];

        data.addColumn('string', 'Urls');
        for (var i = 0; i  < raw_data.length; ++i) {
          data.addColumn('number', raw_data[i][0]);
        }

        data.addRows(years.length);

        for (var j = 0; j < years.length; ++j) {
          data.setValue(j, 0, years[j].toString());
        }
        for (var i = 0; i  < raw_data.length; ++i) {
          for (var j = 1; j  < raw_data[i].length; ++j) {
            data.setValue(j-1, i+1, raw_data[i][j]);
          }
        }

        // Create and draw the visualization.
        new google.visualization.ColumnChart(document.getElementById('visualization')).
            draw(data,
                 { width:800, height:400, backgroundColor: 'fffff4'}
            );
      }


      google.setOnLoadCallback(drawVisualization);
    </script>
    <div id="visualization" style="width: 800px; height: 400px; margin: auto"></div>"""
    return html