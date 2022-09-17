import { Component, OnInit } from '@angular/core';
import {ChartDataset, ChartOptions} from "chart.js";
import {QueryService} from "../../services/query.service";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-query8',
  templateUrl: './query8.component.html',
  styleUrls: ['./query8.component.css']
})
export class Query8Component implements OnInit {

  data_all: any[] = [];
  item: any[] = [];
  quarter: any[]=[];
  sales: any[] = [];

  chartData: ChartDataset[] = [
    {
      type: "pie",
      label: 'quarterwise best sale',
      data: this.sales,
    }
  ];
  chartLabels: string[] = this.quarter;
  chartOptions: ChartOptions = {

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
        backgroundColor: '#ffeaff',
        displayColors: false, // removes unnecessary legend
        padding: 10,

        // ⤵️ title
        titleColor: '#0b4ad2',
        titleFont: {
          size: 18
        },

        // ⤵️ body
        bodyColor: '#2D2F33',
        bodyFont: {
          size: 13
        }
      }
    }
  };

  constructor(private queryService: QueryService, private http: HttpClient) {
  }

  ngOnInit() {
    this.query8Data();
  }

  query8Data(): void {
    this.queryService.getQuery8().subscribe((data: any) => {
        for (const d of data) {
          this.item.push(d.item)
          this.quarter.push(d.quarter)
          this.sales.push(d.sales)
        }
        this.data_all = data;
      }
    )
  }

}

