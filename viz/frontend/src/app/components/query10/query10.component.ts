import { Component, OnInit } from '@angular/core';
import {ChartDataset, ChartOptions} from "chart.js";
import {QueryService} from "../../services/query.service";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-query10',
  templateUrl: './query10.component.html',
  styleUrls: ['./query10.component.css']
})
export class Query10Component implements OnInit {

  data_all: any[] = [];
  Item_name: any[]=[];
  month: any[] = [];
  Sales: any[] = [];

  chartData: ChartDataset[] = [
    {
      type: "pie",
      label: 'Division wise best sale',
      data: this.Sales,
    }
  ];
  chartLabels: string[] = this.month;
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
    this.query10Data();
  }

  query10Data(): void {
    this.queryService.getQuery10().subscribe((data: any) => {
        for (const d of data) {
          this.Item_name.push(d.Item_name)
          this.month.push(d.month)
          this.Sales.push(d.Sales)
        }
        this.data_all = data;
      }
    )
  }

}


