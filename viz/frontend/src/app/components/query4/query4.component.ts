import { Component, OnInit } from '@angular/core';
import {QueryService} from "../../services/query.service";
import {HttpClient} from "@angular/common/http";
import {ChartDataset, ChartOptions} from "chart.js";

@Component({
  selector: 'app-query4',
  templateUrl: './query4.component.html',
  styleUrls: ['./query4.component.css']
})
export class Query4Component implements OnInit {

  data_all: any[] = [];
  year: any[] = [];
  sales: any[] = [];

  chartData: ChartDataset[] = [
    {
      type: "bar",
      label: 'Sales in Taka',
      data: this.sales,
    }
  ];
  chartLabels: string[] = this.year;
  chartOptions: ChartOptions = {
    backgroundColor: '#0014ff',

    // ⤵️ Fill the wrapper
    responsive: true,
    maintainAspectRatio: true,

    // // ⤵️ Remove the grids
    // scales: {
    //   xAxis: {
    //     display: false,
    //     grid: {
    //       drawBorder: false // removes random border at bottom
    //     }
    //   },
    //   yAxis: {
    //     display: false
    //   }
    // },

    plugins: {
      legend: {
        display: true
      },

      tooltip: {
        // ⤵️ tooltip main styles
        backgroundColor: '#ffffff',
        displayColors: true, // removes unnecessary legend
        padding: 10,

        // ⤵️ title
        titleColor: '#D20B0BFF',
        titleFont: {
          size: 18
        },

        // ⤵️ body
        bodyColor: '#ff00ff',
        bodyFont: {
          size: 13
        }
      }
    }
  };

  constructor(private queryService: QueryService, private http: HttpClient) {
  }

  ngOnInit() {
    this.query4Data();
  }

  query4Data(): void {
    this.queryService.getQuery4().subscribe((data: any) => {
        for (const d of data) {
          this.year.push(d.Year)
          this.sales.push(d.Sales)
        }
        this.data_all = data;
      }
    )
  }

}
