import {Component, OnInit} from '@angular/core';
import {ChartDataset, ChartOptions} from "chart.js";
import {query} from "@angular/animations";
import {HttpClient} from "@angular/common/http";
import { QueriesService } from 'src/app/services/queries.service';

@Component({
  selector: 'app-query6',
  templateUrl: './query6.component.html',
  styleUrls: ['./query6.component.css']
})
export class Query6Component implements OnInit {

  data_all: any[] = [];
  division: string[] = [];
  sales: any[] = [];

  chartData: ChartDataset[] = [
    {
      type: "polarArea",
      label: 'Sales in Taka',
      data: this.sales,
    }
  ];
  chartLabels: string[] = this.division
  chartOptions: ChartOptions = {

    // ⤵️ Fill the wrapper
    responsive: true,
    maintainAspectRatio: true,

    // ⤵️ Remove the grids
    scales: {
      xAxis: {
        display: false,
        grid: {
          drawBorder: false // removes random border at bottom
        }
      },
      yAxis: {
        display: false
      }
    },

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

  constructor(private queryService: QueriesService, private http: HttpClient) {
  }

  ngOnInit() {
    this.query6Data();
  }

  query6Data(): void {
    this.queryService.getQuery6().subscribe((data: any) => {
        console.log(data);
        // this.data_all.push(data);
        for(const d of data){
          // console.log(d.division, d.sales);
          this.division.push(d.division);
          this.sales.push(d.sales);
        }
        this.data_all = data;
      }
    )
  }

}