chart_body_00 = {
    "type": "grid-2d",
    "grids": [
        {
            "x": 1,
            "y": 1,
            "h": 4,
            "w": 6,
            "type": "chart",
            "config": {
                "title": {
                    "text": "案由分布"
                },
                "tooltip": {
                    "trigger": "item",
                    "formatter": "{b} : {c} ({d}%)"
                },
                "series": [
                    {
                        "type": "pie",
                        "radius": "55%",
                        "center": ["50%", "60%"],
                        "data": "${chart1}",
                        "itemStyle": {
                            "emphasis": {
                                "shadowBlur": 10,
                                "shadowOffsetX": 0,
                                "shadowColor": "rgba(0,0,0,0.5)"
                            }
                        }
                    }
                ]
            }
        },
        {
            "x": 7,
            "y": 1,
            "h": 4,
            "w": 6,
            "type": "chart",
            "config": {
                title: {
                    text: '各案由时间趋势'
                },
                tooltip: {
                    trigger: 'axis'
                },
                xAxis: {
                    type: 'category',
                    data: "${chart2.year}"
                },
                yAxis: {
                    type: 'value'
                },
                series: "${chart2.data}"
            }
        },
        {
            "x": 1,
            "y": 7,
            "h": 4,
            "w": 6,
            "type": "chart",
            "config": {
                "title": {
                    "text": "类型分布"
                },
                "tooltip": {
                    "trigger": "item",
                    "formatter": "{b} : {c} ({d}%)"
                },
                "series": [
                    {
                        "type": "pie",
                        "radius": "55%",
                        "center": ["50%", "60%"],
                        "data": "${chart3}",
                        "itemStyle": {
                            "emphasis": {
                                "shadowBlur": 10,
                                "shadowOffsetX": 0,
                                "shadowColor": "rgba(0,0,0,0.5)"
                            }
                        }
                    }]
            }
        },
        {
            "x": 7,
            "y": 7,
            "h": 5,
            "w": 6,
            "type": "chart",
            "config": {
                title: {
                    text: '各类型时间趋势'
                },
                tooltip: {
                    trigger: 'axis'
                },
                xAxis: {
                    type: 'category',
                    data: "${chart4.year}"
                },
                yAxis: {
                    type: 'value'
                },
                series: "${chart4.data}"
            }
        }]
};