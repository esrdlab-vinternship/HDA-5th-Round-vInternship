import {Component, OnInit} from '@angular/core';
import {ChartDataset, ChartOptions} from "chart.js";
import {query} from "@angular/animations";
import {HttpClient} from "@angular/common/http";
import { QueriesService } from 'src/app/services/queries.service';

@Component({
  selector: 'app-query9',
  templateUrl: './query9.component.html',
  styleUrls: ['./query9.component.css']
})
export class Query9Component implements OnInit {

  data_all: any[] = [];
  division: string[] = [];
  item_name: string[] = [];  
  sum: any[] = [];

  chartData: ChartDataset[] = [
    {
      type: "polarArea",
      label: 'Sales in Taka',
      data: this.sum,
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
    this.query9Data();
  }

  query9Data(): void {
    this.queryService.getQuery9().subscribe((data: any) => {
        console.log(data);
        // this.data_all.push(data);
        for(const d of data){
          // console.log(d.division, d.sales);
          this.division.push(d.division);
          this.item_name.push(d.item_name);
          this.sum.push(d.sum);
        }
        this.data_all = data;
      }
    )
  }

}