import { Component, OnInit } from '@angular/core';
import {QueryService} from "../../services/query.service";
import {HttpClient} from "@angular/common/http";
import {ChartDataset, ChartOptions} from "chart.js";

@Component({
  selector: 'app-query5',
  templateUrl: './query5.component.html',
  styleUrls: ['./query5.component.css']
})
export class Query5Component implements OnInit {

  data_all: any[] = [];
  district: any[] = [];
  year: any[] = [];
  sales: any[] = [];

  chartData: ChartDataset[] = [
    {
      type: "doughnut",
      label: 'Sales in Taka',
      data: this.sales,

    }
  ];
  chartLabels: string[] = this.district;
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
    this.query5Data();
  }

  query5Data(): void {
    this.queryService.getQuery5().subscribe((data: any) => {
      console.log(data)
        for (const d of data) {
          this.district.push(d.District)
          this.year.push(d.Year)
          this.sales.push(d.Sales)
        }
        this.data_all = data;
      }
    )
  }

}
