import { Component, OnInit } from '@angular/core';
import {ChartDataset, ChartOptions} from "chart.js";
import {QueryService} from "../../services/query.service";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-query6',
  templateUrl: './query6.component.html',
  styleUrls: ['./query6.component.css']
})
export class Query6Component implements OnInit {


  data_all: any[] = [];
  Year: any[] = [];
  district: any[]=[];
  sales: any[] = [];

  chartData: ChartDataset[] = [
    {
      type: "pie",
      label: 'productwise sale',
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
    this.query6Data();
  }

  query6Data(): void {
    this.queryService.getQuery6().subscribe((data: any) => {
        for (const d of data) {
          this.Year.push(d.Year)
          this.district.push(d.district)
          this.sales.push(d.sales)
        }
        this.data_all = data;
      }
    )
  }

}

