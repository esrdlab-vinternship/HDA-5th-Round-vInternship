import { Component, OnInit } from '@angular/core';
import {ChartDataset, ChartOptions} from "chart.js";
import {QueryService} from "../../services/query.service";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-query9',
  templateUrl: './query9.component.html',
  styleUrls: ['./query9.component.css']
})
export class Query9Component implements OnInit {

  data_all: any[] = [];
  Division: any[] = [];
  Item: any[]=[];
  Sales: any[] = [];

  chartData: ChartDataset[] = [
    {
      type: "pie",
      label: 'Division wise best sale',
      data: this.Sales,
    }
  ];
  chartLabels: string[] = this.Division;
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
    this.query9Data();
  }

  query9Data(): void {
    this.queryService.getQuery9().subscribe((data: any) => {
        for (const d of data) {
          this.Division.push(d.Division)
          this.Item.push(d.Item)
          this.Sales.push(d.Sales)
        }
        this.data_all = data;
      }
    )
  }

}


